#!/usr/bin/env python
import sys
import string

currentkey = None
count = 0
count_list = {}

for line in sys.stdin:
    line = line.strip()
    entry = line.split('\t')
    key = entry[0]
    value = entry[1]
    
    if key==currentkey:
        count += 1

    else:
        if currentkey:
            count_list[currentkey] = count
            # renew
            currentkey = key
            count = 1
        else:    
            currentkey = key
            count += 1

count_list[currentkey] = count
sorted_list = sorted(count_list.items(), key=lambda x: x[1],reverse=True)[:20]
for i in range(20):
    temp1 = sorted_list[i][0][1:-1].split(',')[0].strip()[1:-1]
    temp2 = sorted_list[i][0][1:-1].split(',')[1].strip()[1:-1]
    print("%s, %s\t%d" % (temp1,temp2, sorted_list[i][1]))
