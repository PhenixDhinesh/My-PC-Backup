n= int(input())
l=list(map(int,input().split()))
mi,ma=min(l),max(l)
ll=[]
for i in range(1,ma+1):
    ll.append(l.count(i))
print((ll.index(max(ll)))+1)