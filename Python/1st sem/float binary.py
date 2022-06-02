n=input("enter a number\n")
p=int(n)
print(p)
b=[]
while(p>0):
    k=p%2
    b.append(int(k))
    p=p/2
    if(p<2):
        b.append(int(p))
        break
print("\nthe binary value of",n,":")
for i in range(len(b)-1,-1,-1):
    print(b[i],end='')
a=[]
m=n-int(n)
l=m
i=0
if(l!=0):
    while(m!=0):
        k=m%2
        a.append(k)
        m=m/2
        if(m<2):
            a.append(m)
            break
        if(i>3):
            break
        i-i+1
    print(".",end='')
    for i in range(len(a)-1,-1,-1):
        print(a[i],end='')
        
