#!/usr/bin/env python
import sys
import string
import csv


for entry in csv.reader(sys.stdin):
    
    date = entry[1]
    vio_code = entry[2]
    print "%s\t%s" % (vio_code,date)
