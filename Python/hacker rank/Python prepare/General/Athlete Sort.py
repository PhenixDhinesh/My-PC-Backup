p=list(input().split(" "))
p1=int(p[0])
p2=int(p[1])
l=[]
for i in range(p1):
    l1=[]
    k=list(input().split(" "))
    for j in range(p2):
        l1.append(int(k[j]))
    l.append(l1)
n=int(input())
l2=[]
for i in l:
    l2.append(i[n])
l2.sort()
ll=[]
for i in range(len(l2)):
    for j in range(len(l)):
        if l2[i]==l[j][n]:
            ll.append(l[j])
            del l[j]
            break
for i in ll:
        for j in range(len(i)):
            if j==len(i)-1:
                print(i[j],end="\n")
            else:
                print(i[j],end=" ")