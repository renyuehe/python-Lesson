'''
typing模块作用
1.类型检查，防止运行时出现参数和返回值类型不符合。
2.作为开发文档附加说明，方便使用者调用时传入和返回参数类型。
3.该模块加入后并不会影响程序的运行，不会报正式的错误，只有提醒。

注意： typing模块只有在python3.5以上的版本中才可以使用,pycharm目前支持typing检查
'''

import typing


def change_bandwidths(new_bandwidths: typing.Dict,
                      user_id: int,
                      user_name: str) -> bool:

    print(new_bandwidths, user_id, user_name)
    return False


def my_change_bandwidths(new_bandwidths: dict,
                         user_id: int,
                         user_name: str) ->bool:
    print(new_bandwidths, user_id, user_name)
    return True


def main():
    my_id, my_name = 23, "Tiras"
    simple_dict = {"Hello": "Moon"}
    change_bandwidths(simple_dict, my_id, my_name)

    new_dict = {"new": "energy source"}
    my_change_bandwidths(new_dict, my_id, my_name)

if __name__ == "__main__":
    main()