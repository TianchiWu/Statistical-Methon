# 导入模块
from lxml import etree
import requests
import time
# 导入时间模块，防止豆瓣封ip
headers = {
    'User-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
    # 伪装成浏览器
}

url = 'https://movie.douban.com/chart'
# 豆瓣电影排行榜

data = requests.get(url, headers=headers).text
# 给定url并用requests.get()方法来获取页面的text

s = etree.HTML(data)
# 用etree.HTML()来解析下载的页面数据“data”

# title: //*[@id="content"]/div/div[1]/div/div/table[1]/tbody/tr/td[2]/div/a
# xpath: //*[@id="content"]/div/div[1]/div/div/table/tr
file = s.xpath('.//*[@id="content"]/div/div[1]/div/div/table/tr')

time.sleep(3)

scores = '评分: '

evaluate = '一句话评价: '

actor = '上映日期及主演: '

for div in file:
    title = div.xpath("./td[1]/a/@title")[0]
    href = div.xpath("./td[1]/a/@href")[0]
    score=div.xpath("./td[2]/div/div/span[2]/text()")[0]
    num=div.xpath("./td[2]/div/div/span[3]/text()")[0].strip("(").strip().strip(")").strip()
    director = div.xpath("./td[2]/div/p/text()")[0]
    # 截取后半部分的xpath，定位到具体的内容
    print(f"{title},{href},{actor}{director},{scores}{score},{num}\n")
    # 输出爬取到的内容

