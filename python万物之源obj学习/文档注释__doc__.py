# class_doc.py 文档注释
# 文档注释的编写

class Foo(object):
  '''
  这是一个类
  '''

  def method(self, data):
    '''
    这是一个方法
    :param data: 需要的数据
    :return: 返回的数据
    '''
    return "method"


def func(data):
  '''
  这是一个函数
  :param data: 需要的数据
  :return: 返回的数据
  '''
  return "func"



if __name__ == "__main__":
  # 打印文档
  print(Foo.__doc__)
  print(Foo().method.__doc__)

  print(func.__doc__)

