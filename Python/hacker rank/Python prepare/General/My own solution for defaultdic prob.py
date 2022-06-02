n,m=list(map(int,input().split()))
l1=[]
l2=[]
l3=[]
for i in range(n):
    l1.append(input())
for i in range(m):
    l2.append(input())
for i in l2:
    l=[]
    if i not in l1:
        print("-1")
    else:
        for j in range(n):
            if i==l1[j]:
                l.append(str(j+1))
        print(" ".join(l))