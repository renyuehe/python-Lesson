import json

# json.dumps()	将python对象编码成Json字符串
# json.loads()	将Json字符串解码成python对象
# json.dump()	将python中的对象转化成json储存到文件中
# json.load()	将文件中的json的格式转化成python对象提取出来

x = {'name':'你猜','age':19,'city':'四川'}
#用dumps将python编码成json字符串
print(json.dumps(x))
