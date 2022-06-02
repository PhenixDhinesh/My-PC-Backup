import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    s=sum(arr)
    l=[s-x for x in arr if True ]
    print(min(l),max(l),end="\n")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)