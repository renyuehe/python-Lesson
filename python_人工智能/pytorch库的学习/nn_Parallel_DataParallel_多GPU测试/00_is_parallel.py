from torch import nn
def is_parallel(model):
    """check if model is in parallel mode."""
    parallel_type = (
        nn.parallel.DataParallel,
        nn.parallel.DistributedDataParallel,
    )
    return isinstance(model, parallel_type)

from torchvision import models
if __name__ == '__main__':
    rn18 = models.resnet18(pretrained=True)
    ret = is_parallel(rn18)
    print(ret)