nn=int(input())
n=list(map(int,input().split()))
m=int(input())
l=list(map(int,input().split()))
for i in range(m):
    n.append(l[i])
    n=set(n)
    n=list(n)
    n.sort(reverse=True)
    print((n.index(l[i]))+1)