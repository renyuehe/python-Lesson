import re

str = "dog runs to cat"
part1 = "dog"
part2 = "cat"

print(re.search(part2,str))

# ran 或者 run, 方括号代表要给可选项，之选其中一个
part = r"r[au]n"

print(re.search(part,str))
print(re.search(r"r[A-Z]n]",str))
print(re.search(r"r[a-z]n",str))
print(re.search(r"r[0-9]n]",str))

# 更多查询的百度正则字典