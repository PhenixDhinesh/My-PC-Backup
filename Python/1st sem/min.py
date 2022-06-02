print("enter the size of your list")
n=int(input())
a=[]
i=0
print("enter Your list elements")
while(True):
    if(i<n):
        a.append(int(input()))
        i=i+1
    else:
        break
print("this is your list",a)

min=a[0]
while(i<n):
    if(min>a[i]):
        min=a[i]
    i=i+1
    
print(min)
