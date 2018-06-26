from urllib import request
from pprint import pprint
import re


class HuYaSpider:
    url = 'http://www.huya.com/g/lol'
    root_pattern = '<li class="game-live-item" gid="1">([\s\S]*?)</li>'
    title_pattern = '<a[\s\S]*?class="title new-clickstat"[\s\S]*?>([\s\S]*?)</a>'
    name_pattern = '<i class="nick"[\s\S]*?>([\s\S]*?)</i>'
    number_pattern = '<i class="js-num">([\s\S]*?)</i>'

    def __fetch_content(self):
        http = request.urlopen(HuYaSpider.url)
        html = http.read()
        htmlstr = str(html, encoding="utf-8")
        return htmlstr

    def __get_html_roots(self, htmlstr):
        html_roots = re.findall(HuYaSpider.root_pattern, htmlstr)
        return html_roots

    def __get_html_anchors(self, html_roots):
        for root in html_roots:
            yield {
                'name': re.findall(HuYaSpider.name_pattern, root),
                'number': re.findall(HuYaSpider.number_pattern, root),
                'title': re.findall(HuYaSpider.title_pattern, root)
            }

    def __refine(self, anchors):
        def l(anchor):
            return {
                'name': anchor['name'][0].strip(),
                'number': anchor['number'][0].strip(),
                'title': anchor['title'][0].strip()
            }
        return list(map(l, anchors))

    def __sort(self, anchors):
        return sorted(anchors, key=self.__sort__seed, reverse=True)

    def __sort__seed(self, anchor):
        r = re.findall('[\d.]*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        with open('./lol.csv', 'w') as f:
            f.write('name,number,title\n')
            for anchor in anchors:
                f.write(anchor['name']+','+anchor['number'] +
                        ','+anchor['title']+'\n')

    def get_msg(self):
        htmlstr = self.__fetch_content()
        html_roots = self.__get_html_roots(htmlstr)
        anchors = self.__get_html_anchors(html_roots)
        refined_anchors = self.__refine(anchors)
        sorted_anchors = self.__sort(refined_anchors)
        self.__show(sorted_anchors)


if __name__ == '__main__':
    huya_spider = HuYaSpider()
    huya_spider.get_msg()
