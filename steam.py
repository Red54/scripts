import requests
import re
import sys

if len(sys.argv) > 1:
  search = sys.argv[1]
else:
  sys.exit('Need argument')
for i in sys.argv[2:]:
  search += '+' + i
#print(search)
r = requests.get('https://store.steampowered.com/search/?sort_by=Reviews_DESC&publisher='+ search +'&ignore_preferences=1')
#print(r.text)
ms = re.findall('(<span class="title">.*? user reviews for )', r.text, re.S)
games = {}
for m in ms:
  #print(m)
  nm = re.findall('<span class="title">(.*)</span>', m)[0]
  #print(nm)
  rt = re.findall('&lt;br&gt;(.*)%', m)[0]
  #print(rt)
  rv = re.findall('% of the (.*) user reviews for ', m)[0]
  #print(rv)
  pr = int(rv.replace(',', '')) * int(rt) / 100
  #print(pr)
  games[nm] = {'pr': pr, 'rv': rv, 'rt': rt}
for n in sorted(games, key=lambda k: games[k]['pr']):
  g = games[n]
  print(str(g['pr']) + '\t' + g['rv'] + '\t' + g['rt'] + '%\t' + n)
