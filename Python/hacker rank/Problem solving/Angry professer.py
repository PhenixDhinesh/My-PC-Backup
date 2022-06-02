l=[]
for i in range(int(input())):
    n,m=list(map(int,input().split()))
    x=[x for x in list(map(int,input().split())) if x<=0]
    if len(x)<m: l.append("YES")
    else : l.append("NO")
x=[print(x) for x in l]