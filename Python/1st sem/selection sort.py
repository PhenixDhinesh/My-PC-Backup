def selectionsort(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if (a[i]>a[j]):
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
    print("after sorting",a)
    return
a=[]
print("enter the size of the list")
n=int(input())
print("enter the elements of the list")
for i in range(0,n):
    a.append(int(input()))
selectionsort(a)
