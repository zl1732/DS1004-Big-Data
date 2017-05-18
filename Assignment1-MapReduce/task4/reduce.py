#!/usr/bin/env python
import sys
import string

ny_count = 0
other = 0
for line in sys.stdin:
    state = line.strip()
    entry = line.split("\t")
    state = entry[0]
    value = entry[1]


    if state == "NY":
        ny_count += 1
    else:
        other += 1

print "NY\t%d" %  ny_count
print "Other\t%d" %  other
    
