students = [('Tom', 'M', '1005'),
            ('Jerry', 'M', '1003'),
            ('shuke', 'M', '2003'),
            ('Beta', 'M', '2001')]

print(students)
ss1 = sorted(students, key=lambda s: s[2])
print(ss1)

print("------------------")

print(students)
students.sort(key=lambda s: s[2])
print(students)

print("------------------")
print(students)
def func(x):
    return x[0]
students.sort(key=lambda x: func(x))
print(students)