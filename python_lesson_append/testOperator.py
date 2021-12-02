a = 10
b = 3
print(a/b)
print(a//b)

print(4 > 5)
print(4 >= 5)


# 赋值运算
# 赋值运算符: =, +=, -=, *=, **=, /=, %=, //=
var = 10
var += 3
print(var)
var *= 2
print(var)
var = 2
var **= 3
print(var)

var = 9
var /= 2
print(var)

var = 9
var //= 2
print(var)

var = 9
var %= 2
print(var)

# 位运算符 &,  |,   ^
print()
var1 = 5 # 00000101
var2 = 6 # 00000110
ret = var1 & var2   # 4
print(ret)
ret = var1 | var2   # 7
print(ret)
ret = var1 ^ var2   # 3
print(ret)

# 交换值
print()
a, b = 5, 6
print(a,b)
#交换3
# a,00000101
# b,00000110
a = a ^ b
# a,00000011
# b,00000110
b = a ^ b # a^b^b ,其中 a和b异或一次成 a和b的对称态，对称态在异或谁就会变成谁。11的对称态是0,0和0的对称态是0,1两次反转，0两次不变
# a,00000011
# b,00000101
a = a ^ b # a^b^a ,其中 a和b异或一次成 a和b的对称态，对称态在异或谁就会变成谁。11的对称态是0,0和0的对称态是0,1两次反转，0两次不变
# a,00000110
# b,00000101
print(a,b)

#交换1
c = a
a = b
b = c
#交换2
a = a+b
b = a-b
a = a-b
#交换4
a,b = b,a

# 逻辑运算符 and 、 or (相当于 & , |)