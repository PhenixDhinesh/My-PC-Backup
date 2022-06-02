from collections import Counter

n=int(input())
l=Counter(list(map(int,input().split())))
k=[(x//2) for x in l.values() if (x//2)>=1]
print(sum(k))