n=int(input())
s=set(input().split(" "))
k=int(input())
for i in range(k):
    kk=list(input().split(" "))
    d=set(input().split(" "))
    if kk[0]=="intersection_update":
        s.intersection_update(d)
        
    elif kk[0]=="update":
        s.update(d)
       
    elif kk[0]=="symmetric_difference_update":
        s.symmetric_difference_update(d)
        
    elif kk[0]=="difference_update":
        s.difference_update(d)
pp=0
for i in s:
    pp+=int(i)
print(pp)