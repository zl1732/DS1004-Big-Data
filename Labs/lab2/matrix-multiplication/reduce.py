#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import sys
import string
import numpy as np

#number of columns of A/rows of B
n = int(sys.argv[1]) 

#Create data structures to hold the current row/column values (if needed; your code goes here)



currentkey = None
list_a = []
list_b = []

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

    #Remove leading and trailing whitespace
    line = line.strip()

    #Get key/value 
    key, value = line.split('\t',1)

    #Parse key/value input (your code goes here)
    value = value[1:-1].strip()
    value = value.split(',',3)
    value[0] = value[0][1]
    value[2] = float(value[2])


    #If we are still on the same key...
    if key==currentkey:

        #Process key/value pair (your code goes here)
        if value[0]=="A":
            list_a.append(value[2])
        else:
            list_b.append(value[2])
        



    #Otherwise, if this is a new key...
    else:
        #If this is a new key and not the first key we've seen
        if currentkey:

            #compute/output result to STDOUT (your code goes here)
            #print('%s\t%s' % (currentkey,list_a))
            print('%s, %s' % (currentkey,np.sum(np.dot(list_a,list_b))))
            
            ## clear the list for new key, change key
            currentkey = key
            list_a=[]
            list_b=[]
            if value[0]=="A":
                list_a.append(value[2])
            else:
                list_b.append(value[2])


        else:    
            currentkey = key
            #Process input for new key (your code goes here)
            if value[0]=="A":
                list_a.append(value[2])
            else:
                list_b.append(value[2])
        




#Compute/output result for the last key (your code goes here)
print('%s, %s' % (currentkey,np.sum(np.dot(list_a,list_b))))


