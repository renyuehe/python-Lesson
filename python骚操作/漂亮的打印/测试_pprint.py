import pprint
ll = {i: i**2 for i in range(10)}
print(ll)
pprint.pprint(ll)


l2 = [(i, i**2) for i in range(10)]
print(l2)
pprint.pprint(l2)


print("-------------------")
str = pprint.pformat(l2)
print(str)
