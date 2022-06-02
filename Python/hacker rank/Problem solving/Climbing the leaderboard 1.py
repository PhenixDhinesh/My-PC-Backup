import bisect

nn=int(input())
n=list(map(int,input().split()))
m=int(input())
l=list(map(int,input().split()))
n=list(sorted(set(n)))
aa=[bisect.bisect(n,x)for x in l]
for i in aa:
    ab=len(n)+1 - i
    print(ab)