
l = [1,2,3,4,5,6]
l2 = [11,22,33,44,55,66]

w = zip(l, l2)

print(type(w))
ll = []
for i in w:
    print(i)
    ll.append(i)
    print("---------------")
    print(ll)
print("==============")
l3 = zip(*ll)
print(type(l3))
for i in l3:
    print(i)

for i in zip(*ll):
    print(i)

print(",,,,,,,,,,,,")
print(*ll)
