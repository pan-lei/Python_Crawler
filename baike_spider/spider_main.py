# -*- coding:utf-8 -*-
# 主程序,负责根url，以及启动爬虫
from baike_spider import html_downloder
from baike_spider import html_output
from baike_spider import html_parser
from baike_spider import url_manager


class SpilderMain:
    def __init__(self):
        # 初始化所需要的对象,包括url管理器，网页下载器，网页解析器，输出器
        # 来提供给craw（）使用
        # 来提供给craw（）使用
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloder.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutputer()

    def craw(self, url):
        count = 1   # url计数
        # 添加根url
        self.urls.add_new_url(url)
        # 开始解析
        while self.urls.has_new_url():
            try:
                # 获取url
                new_url = self.urls.get_new_url()
                print("第%d个url：%s" % (count, new_url))
                # 将url对应的页面进行下载
                html_cont = self.downloader.download(new_url)
                # 对下载下来的页面进行解析,将解析出来的数据进行保存
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 将解析出来的urls添加到url_manager
                self.urls.add_new_urls(new_urls)
                # 将数据进行收集
                self.outputer.collect_data(new_data)

                if count == 15:
                    break
                count += 1
            except:
                print("爬取失败")

        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpilderMain()
    # 启动爬虫
    obj_spider.craw(root_url)
