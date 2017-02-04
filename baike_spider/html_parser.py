# -*- coding:utf-8 -*-
# 网页解析器
import re
from bs4 import BeautifulSoup
import urllib.parse


class HtmlParser(object):
    # 对html_cont的内容进行解析
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    # 获取页面上所有的url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 根据分析，链接的格式是：/view/12334.htm
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            # url格式需要进行拼接，加上  http://baike.baidu.com
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    # 获取每一页面的数据，包括标题以及简介
    def _get_new_data(self, page_url, soup):
        # 以一个词典数据类型保存数据
        res_data = {}
        # 保存url
        res_data['url'] = page_url
        # 下面是标题的格式
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()
        # 开始获取简介的内容
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data
