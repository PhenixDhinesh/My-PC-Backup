from itertools import combinations

n,m=list(map(int,input().split()))
l=list(map(int,input().split()))
k=0
p=list(combinations(l, 2))
for i in p:
    if sum(list(i))%m==0:
        k+=1
print(k)