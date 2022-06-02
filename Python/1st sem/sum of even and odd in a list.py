a=[]
print("enter the size of the list")
n=int(input())
print("enter the elements of the list")
for i in range(0,n):
    x=int(input())
    a.append(x)
print("here is your list",a)
k=0
b=[]
c=[]
while(k<n):
    if(a[k]%2==0):
        b.append(a[k])
        k=k+1
    else:
        c.append(a[k])
        k=k+1
print("sum of odd numbers in your list",sum(b))
print("sum of even numbers in your list",sum(c))
