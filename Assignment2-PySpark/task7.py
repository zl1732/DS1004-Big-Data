from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader

weekend = ["05", "06", "12", "13", "19", "20", "26", "27"]
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    parking = sc.textFile(sys.argv[1], 1)
    parking = parking.mapPartitions(lambda x: reader(x)) \
                       .map(lambda x: (x[2],(0,1)) if x[1][-2:] in weekend else (x[2],(1,0))) \
 		       .reduceByKey(lambda x,y: (x[0]+y[0], x[1]+y[1]))

    out = parking.map(lambda x: "%s\t%.2f, %.2f" %(x[0],float(x[1][1])/8, float(x[1][0])/23))
    out.saveAsTextFile("task7.out")
    sc.stop()
