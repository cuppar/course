import scrapy
import json
from HuYaScrapy.items import HuYaItem


class Spider(scrapy.Spider):
    name = 'HuYaSpider'
    allowed_domains = ["www.HuYa.com"]
    base_url = 'http://www.huya.com/g/lol'
    start_urls = base_url
    title_pattern = '<a[\s\S]*?class="title new-clickstat"[\s\S]*?>([\s\S]*?)</a>'
    name_pattern = '<i class="nick"[\s\S]*?>([\s\S]*?)</i>'
    number_pattern = '<i class="js-num">([\s\S]*?)</i>'

    def parse(self, response):
        htmlstr = str(response.body, encoding="utf-8")

        def __get_html_roots(self, htmlstr):
            html_roots = re.findall(HuYaSpider.root_pattern, htmlstr)
            return html_roots

        def __get_html_anchors(self, html_roots):
            for root in html_roots:
                yield {
                    'name': re.findall(Spider.name_pattern, root),
                    'number': re.findall(Spider.number_pattern, root),
                    'title': re.findall(Spider.title_pattern, root)
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

        html_roots = self.__get_html_roots(htmlstr)
        anchors = self.__get_html_anchors(html_roots)
        refined_anchors = self.__refine(anchors)
        sorted_anchors = self.__sort(refined_anchors)

        for anchor in sorted_anchors:  # 循环获取每一个主播信息
            item = HuYaItem()
            item['name'] = anchor['name']
            item['title'] = anchor['title']
            item['number'] = anchor['number']
            yield item

        # dont_filter是停止内部过滤
        yield scrapy.Request(url, callback=self.parse, dont_filter=True)
        return

    #	scrapy crawl  HuYaSpider
