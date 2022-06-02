s=input()
k=int(input())
for i in range(len(s)//k):
    o=s[i*k:i*k+k]
    l=[]
    for j in o:
        if j not in l:
            l.append(j)
    print("".join(l))