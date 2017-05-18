#!/usr/bin/env python
import sys
import string

currentkey = None
count = 0
weekend = ["05", "06", "12", "13", "19", "20", "26", "27"]
count_wd = 0
count_we = 0

for line in sys.stdin:
    line = line.strip()
    entry = line.split('\t')
    date = entry[1][-2:]
    vio_code = entry[0]

    if vio_code==currentkey:
        if date in weekend:
            count_we+=1
        else:
            count_wd+=1
    else:
        if currentkey:
            avg_we = float(count_we)/8
            avg_wd = float(count_wd)/23
            print "%s\t%.2f, %.2f" % (currentkey, avg_we, avg_wd)
            
            currentkey = vio_code
            count_we, count_wd =0,0
            if date in weekend:
                count_we+=1
            else:
                count_wd+=1
                
        else:    
            currentkey = vio_code
            if date in weekend:
                count_we+=1
            else:
                count_wd+=1

avg_we = float(count_we)/8
avg_wd = float(count_wd)/23
print "%s\t%.2f, %.2f" % (currentkey, avg_we, avg_wd)
