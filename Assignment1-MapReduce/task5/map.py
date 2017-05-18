#!/usr/bin/env python
import sys
import string
import csv


for entry in csv.reader(sys.stdin):
    
    plate_id = entry[14]
    regis_state = entry[16]

    print "%s\t%s" % ((plate_id, regis_state),1)
