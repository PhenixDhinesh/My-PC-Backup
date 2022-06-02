n=int(input())
l=[]
for i in range(1,n+1):
    ll=[]
    ll.append(str(i))
    oc=oct(i)
    ll.append(str(oc[2:]))
    he=hex(i)
    ll.append(str(he[2:]))
    bi=bin(i)
    ll.append(str(bi[2:]))
    l.append(ll)
for i in range(len(l)):
    for j in range(4):
        k=len(l[n-1][3])
        if j==3:
            print(l[i][j].rjust(k," "),end="\n")
        elif j==2:
            if l[i][j].isdigit()==True:
                print(l[i][j].rjust(k," "),end=" ")
            else:
                m=l[i][j].upper()
                print(m.rjust(k," "),end=" ")
        else:
            print(l[i][j].rjust(k," "),end=" ")