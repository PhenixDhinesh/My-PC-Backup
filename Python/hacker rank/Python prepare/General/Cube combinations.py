a=1
b=1
c=1
n=2
l=[]
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            ll=[i,j,k]
            l.append(ll)
li=[]
for i in range(len(l)):
    p=l[i][0]+l[i][1]+l[i][2]
    if p==n:
        li.append(i)
lio=[]
for i in range(len(l)):
    if i not in li:
        lio.append(l[i])
    
print(lio)

