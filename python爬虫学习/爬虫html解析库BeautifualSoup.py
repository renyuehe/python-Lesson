from urllib.request import urlopen

import bs4.element

urlObj = urlopen(r"https://blog.csdn.net/weixin_40011280/article/details/117766191?spm=1001.2014.3001.5501")

urlContent = urlObj.read()
urlContent = urlContent.decode("utf-8")

from bs4 import BeautifulSoup
soup = BeautifulSoup(urlContent, "lxml")

soup = soup.find_all("p")
# print(len(soup))

for i in soup:
    # aa = bs4.element.Tag # i 的类型，如果不知道 i 有什么函数可以通过预判找到 i 的类型，找到方法后再对 i 编写函数
    try:
        ret = i.find("strong")
        if(ret != None):
            print(ret.get_text())
    except:
        pass






