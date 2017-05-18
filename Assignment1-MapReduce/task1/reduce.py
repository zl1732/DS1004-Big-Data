#!/usr/bin/env python
import sys

currentkey = None
check = 0
for line in sys.stdin:
    line = line.strip()
    summons = line.split('\t')[0]
    value = line.split('\t')[1]
    entry = value.split()
  
    plate_id = entry[0]
    violation_precinct = entry[1]
    violation_code = entry[2]
    issue_date = entry[3]
    index = int(entry[4])

#If we are still on the same key...
    if summons==currentkey:
        check += index

    else:
        if currentkey:
            if check == 1:
                print "%s\t%s, %s, %s, %s" %(temp[0],temp[1],temp[2],temp[3],temp[4])
            currentkey = summons
            temp =  [summons, plate_id,  violation_precinct, violation_code, issue_date, index ]
            check = index
        else:    
            currentkey = summons
            check = index
            temp =  [summons, plate_id,  violation_precinct, violation_code, issue_date, index ]

        
if check == 1:
    print "%s\t%s, %s, %s, %s" %(temp[0],temp[1],temp[2],temp[3],temp[4])
 
