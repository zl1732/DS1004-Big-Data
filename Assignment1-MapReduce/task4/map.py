#!/usr/bin/env python
import sys
import string
import csv

for entry in csv.reader(sys.stdin):
    
    regis_state = entry[16]

    print "%s\t%s" % (regis_state, 1)
