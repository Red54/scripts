import requests
import re
r = requests.get('http://gd.189.cn/gd/sz/fee/bundle/')
r.encoding='gb18030'
#print(r.text)
ms = re.findall('"href="(/support/fee/.*)"', r.text)
r = requests.get('https://gd.189.cn/support/fee/esurfing/')
r.encoding='gb18030'
#print(r.text)
ms += re.findall('"href="(/support/fee/.*)"', r.text)
for m in ms:
  url = 'http://gd.189.cn' + m
  nr = requests.get(url)
  nr.encoding='gb18030'
  if nr.text.find('日封顶') >= 0:
    print(url)
