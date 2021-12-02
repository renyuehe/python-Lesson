from easydict import EasyDict

Cfg = EasyDict()

Cfg.batch = 64
Cfg.dataset_dir = 11111111111

import argparse
def get_args(**kwargs):
    cfg = kwargs
    parser = argparse.ArgumentParser(description='Train the Model on images and target masks',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('-l', '--learning-rate', metavar='LR', type=float, nargs='?', default=0.001,
                        help='Learning rate', dest='learning_rate')

    parser.add_argument('-dir', '--data-dir', type=str, default=r"./",
                        help='dataset dir', dest='dataset_dir')


    args = vars(parser.parse_args())

    # for k in args.keys():
    #     cfg[k] = args.get(k)
    cfg.update(args)

    return EasyDict(cfg)

print(Cfg)
cfg = get_args(**Cfg)  # 获得命令行参数
print(cfg)