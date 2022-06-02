from collections import Counter

ns=int(input())
ls=list(map(int,input().split()))
c=Counter(ls)
ta=0
for i in range(int(input())):
    a=list(map(int,input().split()))
    if c[a[0]]==0:
        continue
    else:
        ta+=a[1]
        c[a[0]]-=1
print(ta)