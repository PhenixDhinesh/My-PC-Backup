from collections import OrderedDict

l=OrderedDict()
for i in range(int(input())):
    k=list(input().split())
    if " ".join(k[:-1]) in l:
        l[" ".join(k[:-1])]+=int(k[-1])
    else:
        l[" ".join(k[:-1])]=int(k[-1])
l=list(l.items())
for i in l:
    print(" ".join(list(map(str,i))))