import requests
from lxml import etree
import pickle
# requests 底层是对python urllib
url = "https://movie.douban.com/top250?start="
urls = [ url+str(index) for index in range(0,226,25)]
data = []
def getPageCon(url):
    global data
    # 数据挖掘
    res = requests.get(url)
    # get方式请求服务器
    # get方式 post方式区别
    # 数据清洗
    html = etree.HTML(res.content)
    titles = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
    info = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/p[2]/span/text()')
    arr = list(zip(titles,info))
    print("正在获取%s的内容"%url)
    data.append(arr)
for url in urls:
    getPageCon(url)
with open("data.txt","wb") as f:
    pickle.dump(data,f)
"""
# 使用 data.txt数据
import pickle

with open("data.txt","rb") as f:
    data = pickle.load(f)
print(data)
"""