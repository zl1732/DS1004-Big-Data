#!/usr/bin/env python
import sys
import csv

for entry in csv.reader(sys.stdin):

    # open have 18 entries, violation have 22 entries
    if len(entry) == 18:
        summons = entry[0]
        print "%s\t%s %s %s %s %s" % (summons,0,0,0,0,-1)
    if len(entry) == 22:
        summons = entry[0]
        plate_id = entry[14]
        violation_precinct = entry[6]
        violation_code = entry[2]
        issue_date = entry[1]
        print "%s\t%s %s %s %s %s" % (summons,plate_id, violation_precinct, violation_code, issue_date,1)

