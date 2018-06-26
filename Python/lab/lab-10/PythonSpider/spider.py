"""爬虫模块"""

from urllib import request  # 模拟Http请求的Python内置库


class Spider:
    """爬虫模块类"""
    url = 'http://www.huya.com/g/lol'  # 类变量，要抓取的网页

    def __fetch__content(self):
        """私有方法，获取网页内容"""
        http = request.urlopen(Spider.url)
        html = http.read()  # bytes,实际上是字节码
        pass

    def get_html(self):
        self.__fetch__content()


spider = Spider()
spider.get_html()

