# bytes 和 str 的互相转换

# bytes --> str:
bytes_data = b'message'
# 方法一：
str_data = str(bytes_data, encoding='utf-8')
# 方法二：
str_data = bytes_data.decode('utf-8')


# str --> bytes:
str_data = 'message'
# 方法一：
bytes_data = bytes(str_data, encoding='utf-8')
# 方法二：
bytes_data = str_data.encode('utf-8')