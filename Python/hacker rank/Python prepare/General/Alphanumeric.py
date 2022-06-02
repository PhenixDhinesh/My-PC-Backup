p=str(input())
l=[[],[],[],[]]
for i in range(len(p)):
    if p[i].isalpha()==True:
        if p[i].isupper()==True:
            l[1].append(p[i])
        else:
            l[0].append(p[i])
            
    elif p[i].isdigit()==True:
        if int(p[i])%2==0:
            l[3].append(p[i])
        else:
            l[2].append(p[i])
l[0].sort()
l[1].sort()
l[2].sort()
l[3].sort()
s=""
for i in range(len(l)):
    for j in range(len(l[i])):
        s+=l[i][j]
print(s)
