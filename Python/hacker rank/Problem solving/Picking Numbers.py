le=int(input())
l=list(map(int,input().split()))
l.sort()
ll=[]
for i in range(le-1):
    for j in range(i+2,le+1):
        ll.append(l[i:j])
p=0
for i in ll:
    if max(i)-min(i)<=1 and p<len(i):
        p=len(i)
print(p)