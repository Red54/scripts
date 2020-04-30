import re
import sys
import math

if len(sys.argv) > 4:
  r = int(sys.argv[1])
  g = int(sys.argv[2])
  b = int(sys.argv[3])
  d = int(sys.argv[4])
else:
  sys.exit('Need argument')

#print(r, g, b)
f = open('color.c')
colors = {}
for x in f:
    color = re.findall('{ "(.*)", (.*), (.*), (.*), 1, .*},', x)
    if len(color) > 0:
        rdiff = abs(int(color[0][1]) - r)
        gdiff = abs(int(color[0][2]) - g)
        bdiff = abs(int(color[0][3]) - b)
        diff = rdiff + gdiff + bdiff
        sqrt = math.sqrt(rdiff ** 2 + gdiff ** 2 + bdiff ** 2)
        if diff <= d:
            print(color[0], diff, sqrt)
