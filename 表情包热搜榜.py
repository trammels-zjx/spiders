import re
import requests
from bs4 import BeautifulSoup
import pprint
from lxml import etree

url = 'https://www.fabiaoqing.com/search/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
r = requests.session()
r = BeautifulSoup(r.get(url, headers=headers).content, "html.parser")
result = r.find('div', {'id': 'othersearch'}).find_all('a')
dic = {}
for i, value in enumerate(result):
    a = value["href"]
    b = re.findall(r"http://fabiaoqing.com/search/bqb/keyword/(.+)", a) 
    dic[i] = b[0]
pprint.pprint(dic)
input1 = int(input("输入号码:"))
url2 = dic[input1]

url1 = 'https://www.fabiaoqing.com/search/search/keyword/'

new_url = url1 + url2

headers = {
    'Host': 'fabiaoqing.com',
    'Referer': 'https://www.fabiaoqing.com/search/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

r = requests.session()

r = r.get(new_url, headers=headers)
print(new_url)
selector = etree.HTML(r.content.decode())

img_name = selector.xpath('//*[@id="bqb"]/div/div')
img_url = selector.xpath('//*[@id="bqb"]/div/div')

l = []
for i in img_name:
    a = i.xpath('a/img/@title')
    b = i.xpath('a/img/@data-original')
    c = i.xpath('a/@href')
    if a==[]:
        continue
    url  = 'http://fabiaoqing.com' + c[0]
    print(a[0])
    print(b[0])
    print(url)
    dic = {}
    with open('img_url.txt', 'a+') as f:
        f.write(b[0] + '\n')

    with open('name.txt', 'a+') as f:
        f.write(a[0] + '\n')

    with open('url.txt', 'a+') as f:
        f.write(url + '\n')


    dic['title'] = a[0]
    dic['img_url'] = b[0]
    dic['url'] = url
    l.append(dic)