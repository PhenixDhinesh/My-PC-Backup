l=[]
for i in range(int(input())):
    n,m=list(map(int,input().split()))
    k=list(map(int,input().split()))
    p=0
    for i in k:
        if i<=0:
            p+=1
    if p<m:
        l.append("YES")
    else:
        l.append("NO")
x=[print(i) for i in l]