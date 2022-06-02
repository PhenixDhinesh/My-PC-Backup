print("enter number of apples")
n=int(input())
print("enter number of persons")
m=int(input())
a=[]
for i in range(0,m):
    a.append(0)
i=0
d=n
l=m
while(d>0):
    a[i]=a[i]+1
    i=i+1
    d=d-1
    if(i==l):
        i=i-l
for i in range(0,m):
    print(a[i])
    i=i+1
