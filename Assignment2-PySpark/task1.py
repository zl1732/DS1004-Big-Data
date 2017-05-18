from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext
from csv import reader

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: wordcount <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    parkings = sc.textFile(sys.argv[1], 1)
    parkings = parkings.mapPartitions(lambda x: reader(x)) \
                       .map(lambda x: (x[0], ", ".join([x[14],x[6],x[2],x[1]])))

    opens = sc.textFile(sys.argv[2], 1)
    opens = opens.mapPartitions(lambda x: reader(x)) \
                 .map(lambda x: (x[0], ", ".join([x[0],"0","0","0","0"]))) 
	
    result = sorted(parkings.subtractByKey(opens).collect()) 	    		     
    out = sc.parallelize(result) \
	    .map(lambda x: "%s\t%s" %(x[0],x[1]))
    
    out.saveAsTextFile("task1.out")
    sc.stop()
