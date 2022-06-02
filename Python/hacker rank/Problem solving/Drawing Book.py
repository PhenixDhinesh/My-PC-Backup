n=int(input())
p=int(input())
s=(n//2)+1
pn=(p//2)+1
l=[]
ll=[]
for i in range(1,s+1):
    l.append(i)
ll.append(l.index(pn))
l.sort(reverse=True)
ll.append(l.index(pn))
print(min(ll))