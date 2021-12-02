# print(" ============ dict 操作 ============")
# a = {"name": "zhang3", "sex": "男", "age": 36}
# print(len(a))
# print(a["name"])
#
# # 修改年龄
# a["age"] = 37
# print(a)
#
# # 添加升高为1.72
# a["height"] = 1.72
# print(a)
#
# # 删除性别属性
# a.pop("sex")
# print(a)

# 任意类型的 key 和 任意类型的value
a = [1,2,3,4]
b = (3,3,3)
dic = {b:"123", "aa":a}
a.append(5)
print(dic[b])
print(dic["aa"])
