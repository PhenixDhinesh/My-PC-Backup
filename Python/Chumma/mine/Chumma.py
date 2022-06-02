l=[]
for i in range(int(input())):
    l.append(int(input()))
for i in l:
    ll=l
    ll.remove(l[i])
    for j in range(len(l)-i):
        print(l[j])
        