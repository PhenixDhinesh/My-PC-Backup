n=int(input("enter a number\n"))
p=n
a=['A','B','C','D','E','F']
c=[]
d=[]
b=[]
while(n>0):
    k=n%2
    b.append(int(k))
    n=n/2
    if(n<2):
        b.append(int(n))
        break
print("the binary value of",p,":")
for i in range(len(b)-1,-1,-1):
    print(b[i],end='')
r=p
while(r>0):
    k=r%8
    c.append(int(k))
    r=r/8
    if(r<8):
        c.append(int(r))
        break
print("\nthe octal value of",p,":")
for i in range(len(c)-1,-1,-1):
    print(c[i],end='')
t=p
while(t>0):
    k=t%16
    d.append(int(k))
    t=t/16
    if(t<16):
        d.append(int(t))
        break
print("\nthe hexal value of",p,":")
for i in range(len(d)-1,-1,-1):
    if(d[i]>10):
        a2=d[i]-10
        d[i]=a[a2]
    print(d[i],end='')
