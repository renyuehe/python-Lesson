import argparse
def get_args():
    parser = argparse.ArgumentParser(prog="test argparse, 默认是文件名",
                                     description='描述',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     usage="usage")

    # 位置参数
    parser.add_argument('param1', type=str, help='姓')
    parser.add_argument('param2', type=str, help='名')

    # 必须参数
    parser.add_argument('--name', type=str, required=True, default='', help='名')

    parser.add_argument('-l', '--learning-rate',
                        metavar='LR',
                        type=float,
                        nargs='?',
                        default=0.001,
                        help='Learning rate',
                        dest='learning_rate')
    # 可选参数
    parser.add_argument('-dir', '--data-dir',
                        type=str,
                        default=r"D:/Desktop",
                        dest='dataset_dir')

    return parser.parse_args()


cfg = get_args()
print(cfg)