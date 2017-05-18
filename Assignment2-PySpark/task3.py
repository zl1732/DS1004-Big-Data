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
    opens = sc.textFile(sys.argv[1], 1)
    opens = opens.mapPartitions(lambda x: reader(x)) \
                       .map(lambda x: (x[2],(float(x[12]),1))) \
 		       .reduceByKey(lambda x,y: (x[0]+y[0],x[1]+y[1]))

    out = opens.map(lambda x: "%s\t%.2f, %.2f" %(x[0],x[1][0],float(x[1][0]/x[1][1])))
    out.saveAsTextFile("task3.out")
    sc.stop()
