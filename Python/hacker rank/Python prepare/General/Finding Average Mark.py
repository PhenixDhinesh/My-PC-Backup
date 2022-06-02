n=int(input())
d={}
for i in range(n):
    m=list(input().split(" "))
    d.update({m[0]:m[1:]})
k=d.get(input())
kk=0
for i in k:
    j=float(i)
    kk+=j
kkk=k/3
print ('%.2f'%kkk)
    
