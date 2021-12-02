import torch.nn as nn
import torch
import cv2
import numpy as np

# convert uint (HxWxn_channels) to 3-dimensional torch tensor
def uint2tensor3(img):
    if img.ndim == 2:
        img = np.expand_dims(img, axis=2) #升维
    return torch.from_numpy(np.ascontiguousarray(img)).permute(2, 0, 1).float().div(255.) #内存连续,换轴,归一化

# convert torch tensor to uint
def tensor2uint(img):
    img = img.data.squeeze().float().clamp_(0, 1).cpu().numpy()
    if img.ndim == 3:
        img = np.transpose(img, (1, 2, 0)) # 换轴
    return np.uint8((img*255.0).round()) # 四舍五入

def imsave(img, img_path):
    if img.ndim == 3:
        img = img[:, :, [2, 1, 0]] # 换轴
    cv2.imwrite(img_path, img)

def readimage(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)  # BGR or G
    if img.ndim == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)  # GGG
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def test():
    img=readimage('small_girl.jpg')
    print(img.shape)#(400, 600, 3)
    x=uint2tensor3(img) # 结果：三通道,归一化,chw
    print(x.shape)#torch.Size([3, 400, 600])
    x=torch.unsqueeze(x,dim=0)
    print(x.shape)  #torch.Size([1, 3, 400, 600])

    # 均值
    mean = nn.Parameter(torch.Tensor([0.485, 0.456, 0.406]).reshape(1, 3, 1, 1), requires_grad=False)
    # 标准差
    std = nn.Parameter(torch.Tensor([0.229, 0.224, 0.225]).reshape(1, 3, 1, 1), requires_grad=False)

    # mean.repeat 代表重复,就是翻倍.  对指定轴上的值repeat
    # 原图 - 均值
    x = x - mean.repeat(x.size(0), 1, x.size(2), x.size(3)) # (1, 1, 540, 960)
    si = tensor2uint(x) # 归一化到 - 和 + 之间, 还原成 255 值大小
    imsave(si, 'mean2.png') # 就是保留了均值以上的像素值

    # (原图 - 均值) / 标准差
    x = x / std.repeat(x.size(0), 1, x.size(2), x.size(3))
    si=tensor2uint(x)
    imsave(si, 'mean_std2.png')

test()