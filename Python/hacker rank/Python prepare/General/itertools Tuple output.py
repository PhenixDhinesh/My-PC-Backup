l1=list(map(int,input().split(" ")))
l2=list(map(int,input().split(" ")))
l3=[]
l1.sort()
l2.sort()
for i in l1:
    for j in l2:
        l=[]
        l.append(i)
        l.append(j)
        print(tuple(l),end=(" "))