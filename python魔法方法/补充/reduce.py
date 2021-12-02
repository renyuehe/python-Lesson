
class ServerError(UserWarning):
    # UserWarning用户代码生成的警告
    def error(self):
        # C语言接口，可将错误信息pickle成字符串
        return self.__reduce__()[1]

#返回的是(<class '__main__.ServerError'>, ('错误信息',))，所以切片取1

def instance_name(name):
    try:
        if not isinstance(name,str):
            raise ServerError("名字必须是字符串")
    except ServerError as e:
        error=e.error()[0]
        print(error)

instance_name(123)
#作用是：可以将自定义的错误信息，组成json格式返回给前端