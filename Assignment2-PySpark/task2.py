from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    parkings = sc.textFile(sys.argv[1], 1)
    counts = parkings.mapPartitions(lambda x: reader(x)) \
                       .map(lambda x: (x[2], 1)) \
		       .reduceByKey(lambda x,y: x+y) \
                       .map(lambda x: "%s\t%s" % (x[0],x[1]))
    counts.saveAsTextFile("task2.out")
    sc.stop()
