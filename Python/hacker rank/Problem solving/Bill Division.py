n,m=list(map(int,input().split()))
l=list(map(int,input().split()))
a=int(input())
del l[m]
if (sum(l))/2==a:
    print("Bon Appetit")
else:
    print(int(a-(sum(l))/2))