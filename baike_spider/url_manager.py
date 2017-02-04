# -*- coding:utf-8 -*-
# url管理器


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 添加url
    def add_new_url(self, url):
        if url is None:
            return
        # 当url既不在新的列表中也不在旧的列表中时，则将其添加到新的url——set()集合中
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断是否还有待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url