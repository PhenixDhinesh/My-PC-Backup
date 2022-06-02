from itertools import combinations

s,n=list(input().split())
l=[]
for i in range(1,int(n)+1):
    lk=[]
    ll=list(combinations(s,i))
    for j in ll:
        j=list(j)
        j.sort()
        lk.append("".join(j))
    lk.sort()
    l.append(lk)
for i in l:
    for j in i:
        print(j)