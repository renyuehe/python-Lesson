from urllib.request import urlopen

import json

url = urlopen(r"http://v.juhe.cn/joke/randJoke.php?key=505de17bf25e602ce27436b1403503f8")
url_content = url.read().decode("utf-8")

print(url_content)

json_dict = json.loads(url_content)
print(json_dict)

a = {"123":123}

result = json_dict.get("result")
print(result)
for i in result:
    print(i.get("content"))
    print("\n")



