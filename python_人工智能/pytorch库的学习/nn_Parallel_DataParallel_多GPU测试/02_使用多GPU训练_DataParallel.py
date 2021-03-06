import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader

# 虚拟构造一个数据集
class RandomDataset(Dataset):
    def __init__(self, size, length):
        self.len = length
        self.data = torch.randn(length, size)
    def __getitem__(self, index):
        return self.data[index]
    def __len__(self):
        return self.len

class Model(nn.Module):
    # 我们的模型
    def __init__(self, input_size, output_size):
        super(Model, self).__init__()
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, input):
        output = self.fc(input)
        print("\tIn Model: input size", input.size(),
              "output size", output.size())

        return output

input_size = 5
output_size = 100
rand_loader = DataLoader(dataset=RandomDataset(input_size, output_size),
                         batch_size=30,
                         shuffle=True)


model = Model(input_size, output_size)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

if torch.cuda.device_count() > 1:
  print("Let's use", torch.cuda.device_count(), "GPUs!")
  # dim = 0 [30, xxx] -> [10, ...], [10, ...], [10, ...] on 3 GPUs
  model = nn.DataParallel(model)


for data in rand_loader:
    input = data.to(device)
    output = model(input)
    print("Outside: input size", input.size(),
          "output_size", output.size())



