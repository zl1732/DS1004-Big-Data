#!/usr/bin/env python
import sys
import string

currentkey = None
count = 0
add = 0
for line in sys.stdin:
    line = line.strip()
    entry = line.split('\t')
    ls_type = entry[0]
    amount = float(entry[1])
    
    
    if ls_type==currentkey:
        count += 1
        add += amount

    else:
        if currentkey:
            count+=1
            print "%s\t%.2f, %.2f" % (currentkey, add, add/count)
            currentkey = ls_type
            count = 0
            add = amount
        else:    
            currentkey = ls_type
            add += amount

print "%s\t%.2f, %.2f" % (currentkey, add, add/(count+1))

