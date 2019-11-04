import requests
import re
import html

url = 'https://www.vmall.com/list-36-%s-1-1'
vmall = 'https://www.vmall.com'

for i in range(1, 4):
	curl = url % i
	r = requests.get(curl)
	phones = re.findall('<p class="p-img"><a target="_blank" href="(.*?)"', r.text)
	for x in phones:
		purl = vmall + x
		pr = requests.get(purl)
		text = html.unescape(pr.text)
		if '红外' in text:
			print(purl)
			title = re.findall('title>(.*)</title', text)[0]
			print(title)
			ir = re.findall('(.*红外.*)', text)
			print(ir)
			print()

