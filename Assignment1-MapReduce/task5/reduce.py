#!/usr/bin/env python
import sys
import string

currentkey = None
count = 0
max_count = 1 
max_key = None

for line in sys.stdin:
    line = line.strip()
    key = line.split("\t")[0]
    value = line.split("\t")[1]

    
    if key==currentkey:
        count += 1

    else:
        if currentkey:
            if count > max_count:
                max_count = count
                max_key = currentkey

            currentkey = key
            count = 1
        else:    
            currentkey = key
            count += 1
            max_key = key

if count > max_count:
    max_count = count
    max_key = currentkey          
temp1 = max_key[1:-1].split(',')[0].strip()[1:-1]
temp2 = max_key[1:-1].split(',')[1].strip()[1:-1]
print("%s, %s\t%d" % (temp1,temp2,max_count))


