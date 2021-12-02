
import torch


torch.distributed.init_process_group(backend, init_method='env://', **kwargs)