n,m=list(map(int,input().split()))
l=max(list(map(int,input().split())))
if m<l:print(abs(l-m))
else:print(0)