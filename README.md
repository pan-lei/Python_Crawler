## Python实现的爬虫

test文件夹下是对用到的网页下载器urllib和网页解析器BeautifulSoup的测试

baike_spider是项目文件

该轻量级的爬虫是对百度百科中由Python词条地址为根url进行爬取，

爬取页面中的url，以及页面词条名称以及简介

若爬取到的url未进行过爬取则循环进行爬取

将爬取到的标题和简介保存到一个html文件中，并进行输出

限定爬取15条。
