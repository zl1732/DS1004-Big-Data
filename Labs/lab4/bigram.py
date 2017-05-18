from __future__ import print_function

import sys
from operator import add
from pyspark import SparkContext


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: bigram <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    lines = sc.textFile(sys.argv[1], 1)
    sentences = lines.glom() \
                  .map(lambda x: " ".join(x)) \
                  .flatMap(lambda x: x.split("."))

    #Your code goes here
    bigrams = sentences.flatMap(lambda x: [(x.split(" ")[i],x.split(" ")[i+1]) for i in range(0, len(x.split(" "))-1)]) \
                  .map(lambda x: (x,1)) \
                  .reduceByKey(add)  \
                  .sortBy(lambda x: x[1], False) \
                  .take(100)  
    out=sc.parallelize(bigrams)
    out.saveAsTextFile("bigrams.out")
    sc.stop()
