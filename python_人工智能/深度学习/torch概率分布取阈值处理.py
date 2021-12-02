import torch

if __name__ == '__main__':
    out = torch.randn((5,5))
    print(out)
    out = torch.where(out > 0.5, 1, 0)
    print(out)
    pass