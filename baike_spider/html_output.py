# -*- coding:utf-8 -*-
# 最后的结果输出
# 提供两个功能，一个事收集数据，另一个是输出数据


class HtmlOutputer(object):
    # 收集数据需要一个列表list进行维护
    def __init__(self):
        self.datas= []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    # 输出一个html文档
    def output_html(self):
        fileout = open("output.html", "w", encoding='utf-8')
        fileout.write("<html>")
        fileout.write("<head>")
        fileout.write("<meta charset=\'utf-8\'>")
        fileout.write("</head>")
        fileout.write("<body>")
        fileout.write("<table>")
        for data in self.datas:
            fileout.write("<tr>")
            fileout.write("<td>%s</td>" % data['url'])
            fileout.write("<td>%s</td>" % data['title'])
            fileout.write("<td>%s</td>" % data['summary'])
            fileout.write("</tr>")
        fileout.write("</table>")
        fileout.write("</body>")
        fileout.write("</html>")
        fileout.close()
