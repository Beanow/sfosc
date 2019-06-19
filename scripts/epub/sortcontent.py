#! /usr/bin/env python
from __future__ import print_function
import bisect
import frontmatter
import pprint
import os

print('Retreiving input filenames and ordering them...')
md = ['content/_index.md']
for (root, dirs, files) in os.walk('content'):
    flist = []
    for d in dirs:
        f = root+'/'+d+'/_index.md'
        page = frontmatter.load(f)
        weight = page['weight'] if 'weight' in page else 0
        flist.append((f, weight))
    pprint.pprint(flist)

    for f in files:
        if f == '_index.md':
            continue
        f = root+'/'+f
        page = frontmatter.load(f)
        weight = page['weight'] if 'weight' in page else 0
        flist.append((f, weight))

    flist.sort(key = lambda x: x[1])
    oflist = [ft[0] for ft in flist]
    if len(oflist) == 0:
        continue
    pprint.pprint(oflist)

    index = bisect.bisect(md, oflist[0])
    for f in oflist:
        md.insert(index, f)
        index += 1
    
    pprint.pprint(md)

print('Writing order to order.txt file...')
pprint.pprint(md)
orderFile=open('order.txt','w')
print(' '.join(md), file=orderFile)
orderFile.close()
