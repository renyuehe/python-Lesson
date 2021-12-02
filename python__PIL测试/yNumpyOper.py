import numpy
from functools import reduce

class NumpyOperator():

    def ndarrayWrapper(self, ndarr: numpy.ndarray, axis:tuple, len:int=0, mode:str="wrap", value=0) -> numpy.ndarray:
        # 对一个张量实现指定轴s的扩张与收缩
        '''
        :param ndarr: 准备被膨胀的数组
        :param axis: 膨胀的维度
        :param len: 膨胀的长度 默认 1
        :param mode: 膨胀模式 默认 wrap
        :param value: 膨胀值 默认 0
        :return: 被膨胀完成的张量
        '''
        l = self._generate_std_list(ndarr.shape)
        permList = self.perFirst(l)

        for i in range(permList.__len__()):

            if i in axis:
                ndarr = numpy.transpose(ndarr, tuple(permList[i]))#转换过去
                ndarrShape = list(ndarr.shape)
                ndarrShape[0] = len;

                ln = reduce(lambda x, y: x * y, ndarrShape)
                cutarr = numpy.arange(ln).reshape(ndarrShape)
                cutarr.astype(ndarr.dtype)
                cutarr *= 0
                cutarr += 1
                cutarr *= value

                if mode == "wrap":
                    ndarr = numpy.concatenate((cutarr, ndarr, cutarr), axis=0)
                elif mode == "pre":
                    ndarr = numpy.concatenate((cutarr, ndarr), axis=0)
                elif mode == "tail":
                    ndarr = numpy.concatenate((ndarr, cutarr), axis=0)

                ndarr = numpy.transpose(ndarr, tuple(permList[i]))#转换回去
        return ndarr

    def perFirst(self, arr):
        # 0 号 和每个其他位置元素的换位置
        l = self._generate_std_list(arr)
        length = len(l)

        if length == 1:
            return [arr]

        print(length)
        result = [] #存储结果
        for i in range(length):
            templ1 = l.copy()
            tmp = templ1[i]
            templ1[i] = l[0]
            templ1[0] = tmp

            result.append(templ1)
        return result

    def fullPermutation(self, arr):
        """实现全排列"""
        length = len(arr)
        if length == 1:  # 递归出口
            return [arr]

        result = []  # 存储结果
        fixed = arr[0]
        rest = arr[1:]

        for _arr in self.fullPermutation(rest):  # 遍历上层的每一个结果
            for i in range(0, length):  # 插入每一个位置得到新序列
                new_rest = _arr.copy()  # 需要复制一份
                new_rest.insert(i, fixed)
                result.append(new_rest)
        return result

    def _generate_std_list(self, tp:tuple) -> list:
        len(tp)
        l = []
        for i in range((len(tp))):
            l.append(i)
        return l

if __name__ == "__main__":
    numpyOper = NumpyOperator()

    ret = numpyOper.perFirst((3,4,5,6,7))
    print(ret)
    ret = numpyOper.fullPermutation([0,1,2,3])
    for i in ret:
        print(i)

    a = numpy.arange(8).reshape(2,2,2)
    a = a.astype(numpy.int32)
    ret = numpyOper.ndarrayWrapper(ndarr=a, axis=(0,), mode="wrap", len=1, value=10)
    print(ret)