students = [('Tom', 'M', '1005'),
            ('Jerry', 'M', '1003'),
            ('shuke', 'M', '2003'),
            ('Beta', 'M', '2001')]


# 默认排序（按照姓名首字母排序：B<J<T<s排序）
print(sorted(students))
# [('Beta', 'M', '2001'), ('Jerry', 'M', '1003'), ('Tom', 'M', '1005'), ('shuke', 'M', '2003’)]

# 按元组内第3个元素排序（按照学号排序：1003<1005<2001<2003排序）
print(sorted(students, key=lambda s: s[2]))
# [('Jerry', 'M', '1003'), ('Tom', 'M', '1005'), ('Beta', 'M', '2001'), ('shuke', 'M', '2003')]

# 3、利用sorted函数对【字典】进行排序
student_dict1 = {'Jerry':'1003',
                 'Tom':'1005',
                 'Beta':'2001',
                 'Shuke':'2003'}

# 输出字典的键和值
print(student_dict1.items())
# dict_items([('Jerry', '1003'), ('Tom', '1005'), ('Beta', '2001'), ('Shuke', '2003')])

# 按照字典的【键】排序
print(sorted(student_dict1.items(), key=lambda d: d[0]))
# [('Beta', '2001'), ('Jerry', '1003'), ('Shuke', '2003'), ('Tom', '1005')]

# 按照字典的【值】排序
result = sorted(student_dict1.items(), key=lambda d: d[1])
print(result)

# 将结果转换为字典
print(dict(result))
# {'Jerry': '1003', 'Tom': '1005', 'Beta': '2001', 'Shuke': '2003'}