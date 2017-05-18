#!/usr/bin/env python
import sys
import string

currentkey = None
count = 0
for line in sys.stdin:
    line = line.strip()
    entry = line.split('\t')
    vio_code = entry[0]
    value = entry[1]

    if vio_code==currentkey:
        count += 1
    else:
        if currentkey:
            count+=1
            print "%s\t%d" % (currentkey, count)
            currentkey = vio_code
            count = 0
        else:    
            currentkey = vio_code


print "%s\t%d" % (currentkey, count+1)
