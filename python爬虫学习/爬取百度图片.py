import requests
import os
import urllib


class Spider_baidu_image():
    def __init__(self):
        self.url = 'http://image.baidu.com/search/acjson?'
        # 浏览器 ID（用来告诉服务器用户信息，系统版本、浏览器等等） 如果没有这个 ID ，那么服务器是知道不是通过浏览器访问的，就会施行反爬虫机制，加了这个 ID 就相当于是反反爬虫
        # 其中 refer 是参考网址，说白了就是百度有反爬虫技术，那么我们就用他自己的生成好的网址模型作为参考，只替换其中的查找的单词的图片就好了
        # User-Agent 是必须的，这样才能伪装成浏览器进行访问，为了反反爬虫技术，如果没有这个东西，百度服务器就知道不是浏览器再访问，因为浏览器默认都会加这几个参数。
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.\
            3497.81 Safari/537.36'}
        self.headers_image = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.\
            3497.81 Safari/537.36',
            # 'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1557124645631_R&pv=&ic=&nc=1&z=&hd=1&latest=0&copyright=0&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&sid=&word=%E8%83%A1%E6%AD%8C'
            'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%C3%C0%C5%AE&fr=ala&ala=1&alatpl=normal&pos=0'}
        # self.keyword = '刘亦菲壁纸'
        self.keyword = input("请输入搜索图片关键字:")
        self.paginator = int(input("请输入搜索页数，每页30张图片："))
        # self.paginator = 50
        # print(type(self.keyword),self.paginator)
        # exit()

    def get_param(self):
        """
        获取url请求的参数，存入列表并返回
        :return:
        """
        keyword = urllib.parse.quote(self.keyword)
        params = []
        for i in range(1, self.paginator + 1):
            params.append(
                # 这里的 请求参数不知道怎么搜集 ，暂时用这里默认的的就行了，
                'tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=1&latest=0&copyright=0&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&cg=star&pn={}&rn=30&gsm=78&1557125391211='.format(
                    keyword, keyword, 30 * i))
        return params

    def get_urls(self, params):
        """
        由 url参数 返回各个url 拼接后的响应，存入列表并返回
        :return:
        """
        urls = []
        for i in params:
            urls.append(self.url + i)
        return urls

    def get_image_url(self, urls):
        image_url = []
        for url in urls:
            json_data = requests.get(url, headers=self.headers).json()
            json_data = json_data.get('data')

            for i in json_data:
                if i:
                    image_url.append(i.get('thumbURL'))
        return image_url

    def get_image(self, image_url):
        """
        根据图片url，在本地目录下新建一个以搜索关键字命名的文件夹，然后将每一个图片存入。
        :param image_url:
        :return:
        """
        cwd = os.getcwd()
        file_name = os.path.join(cwd, self.keyword)
        if not os.path.exists(self.keyword):
            os.mkdir(file_name)
        for index, url in enumerate(image_url, start=1):
            with open(file_name + '\\{}.jpg'.format(index), 'wb') as f:
                f.write(requests.get(url, headers=self.headers_image).content)
            if index != 0 and index % 30 == 0:
                print('{}第{}页下载完成'.format(self.keyword, index / 30))

    def __call__(self, *args, **kwargs):
        params = self.get_param()               # 获取 url 请求参数
        print(params)

        urls = self.get_urls(params)            # 获取 urls
        # print(urls)
        for i in urls:
            print(i)
        image_url = self.get_image_url(urls)    # 获取 image_url
        for i in image_url:
            print(i)
        self.get_image(image_url)


if __name__ == '__main__':
    spider = Spider_baidu_image()
    spider()
