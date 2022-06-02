from itertools import combinations_with_replacement

s,m=input().split()
s=list(s)
s.sort()
s=''.join(s)
l=list(combinations_with_replacement(s,int(m)))
for i in l:
    print(''.join(i))