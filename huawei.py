import requests
import re
import html

url = 'https://openapi.vmall.com/mcp/queryPrd?lang=zh-CN&country=CN&portal=1&keyword=36&pageSize=200&searchSortField=1&searchSortType=asc&searchFlag=1'
vmall = 'https://www.vmall.com/product/%s.html'

r = requests.get(url)
phones = re.findall('productId":(.*?),', r.text)
for x in phones:
    purl = vmall % x
    pr = requests.get(purl)
    text = html.unescape(pr.text)
    if '红外' in text:
        print(purl)
        title = re.findall('title>(.*)</title', text)[0]
        print(title)
        ir = re.findall('(.*红外.*)', text)
        print(ir)
        print()
