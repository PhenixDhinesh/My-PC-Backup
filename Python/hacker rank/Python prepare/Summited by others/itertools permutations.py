from itertools import permutations
a=list(input().split())
l=list(a[0])
b=int(a[1])
l1=list(permutations(l,b))
for i in l1:
    print(''.join(i))