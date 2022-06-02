import math
import os
import random
import re
import sys

def breakingRecords(scores):
# From Here to

    l=scores
    res=[0,0]
    ma=l[0]
    mi=l[0]
    for i in range(1,len(l)):
        if l[i]>ma:
            res[0]+=1
            ma=l[i]
        elif l[i]<mi:
            res[1]+=1
            mi=l[i]
    return res
    
#Here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
