# 导入相应的包
from bs4 import BeautifulSoup
import requests
import re
import datetime

# 获取当前时间并指定格式为2018041018
time = datetime.datetime.now().strftime("%Y%m%d%H")
url = r'https://66bang.com/home/#/e-business/video'
# 模拟真实浏览器进行访问
headers = {
    'User-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'
}

response = requests.get(url, headers=headers,auth=('13771193626', 'Wtc20000229'))

page_html = response.text

soup = BeautifulSoup(page_html, 'html.parser')

titles = soup.find('div')

print(titles)