#!/usr/bin/env python
import sys
import string
import csv

for entry in csv.reader(sys.stdin):
    vio_code = entry[2]
    print "%s\t%d" % (vio_code, 1) 
