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
    parking = sc.textFile(sys.argv[1], 1)
    parking = parking.mapPartitions(lambda x: reader(x)) \
                       .map(lambda x: ((x[14],x[16]),1)) \
 		       .reduceByKey(lambda x,y: x+y) \
		       .sortBy(lambda x: x[1], False) \
		       .take(1)
    parking = sc.parallelize(parking)
    out = parking.map(lambda x: "%s, %s\t%d" %(x[0][0],x[0][1],x[1]))
    out.saveAsTextFile("task5.out")
    sc.stop()
