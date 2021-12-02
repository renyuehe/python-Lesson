import re

import requests
import os
import urllib

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.\
    3497.81 Safari/537.36'}
headers_image = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.\
    3497.81 Safari/537.36',
    'Referer': 'http://image.baidu.com'
    # 'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C3%C0%C5%AE&fr=ala&ala=1&alatpl=normal&pos=0'
    }

# pn , word , queryword
url =  "http://image.baidu.com/search/index?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=1&latest=0&copyright=0&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=star&pn={}&rn=30&gsm=78&1557125391211="
# self.keyword = '刘亦菲壁纸'
keyword = input("请输入搜索图片关键字:")
keyword_utf8 = urllib.parse.quote(keyword, "utf-8")

if os.path.isdir(keyword) != True:
    os.makedirs(keyword)

n = 0
j = 0

while (n < 3000):
    n += 30

    urll = url.format(keyword_utf8, str(n))
    rep = urllib.request.Request(urll,  headers=headers_image)
    rep = urllib.request.urlopen(rep)
    try:
        result = rep.read().decode("utf-8")
        # 正则表达式
        reg = re.compile(r"thumbURL.*?\.jpg")
        thumbURLList = reg.findall(result)

        for i in thumbURLList:
            i = i.replace('thumbURL":"','')
            print(i)
            urllib.request.urlretrieve(i, keyword+"/pic_{num}.jpg".format(num=j))
            j+=1

    except:
        print("error")


