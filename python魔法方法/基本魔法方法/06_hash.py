'''
python中 hash(o) 接收一个 不可变类型 的数据作为参数，提取数据的特征码，特征码是整数

相同的数据 -> 相同的结果

运行 print(hash("Traditional")) 多次，可以得到不同的结果。想要了解这个现象背后的原因，需要学习hash运算的原理。

在运行时发现了一个现象：相同字符串在同一次运行时的哈希值是相同的，但是不同次运行的哈希值不同。
这是由于Python的字符串hash算法有一个启动时随机生成secret prefix/suffix的机制，存在随机化现象：对同一个字符串输入，不同解释器进程得到的hash结果可能不同。因此当需要做可重现可跨进程保持一致性的hash，需要用到hashlib模块。[1]
'''

def main():
    print(hash(1234556))
    print("---")
    print(hash("Traditional"))
    print("---")
    print(hash((1, 2, 3, 4)))

    # list
    lt = [1, 2]
    print(hash(lt)) # 不可以被 hash

if __name__ == '__main__':
    main()