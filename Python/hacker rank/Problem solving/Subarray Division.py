n=int(input())
l=list(map(int,input().split()))
d,m=list(map(int,input().split()))
p=0
for i in range(n-m+1):
    if sum(l[i:i+m])==d:
        p+=1

print(p)