import os
import sys


def getMoneySpent(keyboards, drives, b):
# here
    l=[]
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i]+drives[j]<=b:
                l.append(keyboards[i]+drives[j])
    if len(l)==0:
        return -1
    else:
        return max(l)
# here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
