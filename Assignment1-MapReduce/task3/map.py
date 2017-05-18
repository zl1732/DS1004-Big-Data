#!/usr/bin/env python
import sys
import string
import csv


for entry in csv.reader(sys.stdin):

    ls_type = entry[2]
    amount = float( entry[12])

    print "%s\t%s" % (ls_type, amount)
