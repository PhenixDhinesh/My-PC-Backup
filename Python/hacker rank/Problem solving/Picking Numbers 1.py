le=int(input())
l=list(map(int,input().split()))
l.sort()
p=0
for i in range(le-1):
    ll=[]
    for j in range(i+2,le+1):
        ll=l[i:j]
        if max(ll)-min(ll)<=1 and p<len(ll):
            p=len(ll)
print(p)