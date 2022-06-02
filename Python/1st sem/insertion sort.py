def insertionsort(a):
    for i in range(0,len(a)):
        current=a[i]
        pos=i
        while(pos>0 and a[pos-1]>current):
            a[pos]=a[pos-1]
            pos=pos-1
        a[pos]=current
    return
a=[]
print("enter the size of the list")
n=int(input())
print("enter the elements of the list")
for i in range(0,n):
    a.append(int(input()))
insertionsort(a)
print("after sorting\n",a)
