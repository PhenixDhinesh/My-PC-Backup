ll=[]
s=[]
for i in range(int(input())):
    l=[]
    a=input()
    b=float(input())
    l.append(a)
    l.append(b)
    ll.append(l)
    s.append(b)
    

s.sort()

ss=0
for i in range(len(s)):
    if s[0]<s[i+1]:
        ss=ss+s[i+1]
        break
print(ss)
p=[]
for i in range(len(ll)):
    if ll[i][1]==ss:
        p.append(ll[i][0])
p.sort()
for x in p:
    print(x)
     
    
        

    