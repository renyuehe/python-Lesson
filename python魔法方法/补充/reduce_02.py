
from functools import reduce

'''
reduce，有减少，降低，归纳的意思。
reduce() 函数会对参数序列中元素进行“累积”。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
'''

#示例一：求列表数据的和
print(reduce(lambda x, y : x+y, [1,2,3,4,5]))


# #示例二：拼字符串
# lst5 = ['a','Ab','ABC','abcd','Abcde','cc']
# print(reduce(lambda x,y:x+y, lst5))
#
#
# #示例三：找出列表中的最大值
# def abc(x,y):
#     if x>y:
#         return x
#     else:
#         return y
#
#
# lst4 = [5,2,7,2,1]
# print(reduce(abc, lst4))

