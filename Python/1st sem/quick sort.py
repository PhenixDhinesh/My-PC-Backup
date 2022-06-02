def quicksort(mylist):
    x=[]
    y=[]
    z=[]
    if(len(mylist)>1):
        pivot=mylist[0]
        for i in mylist:
            if i<pivot:
                x.append(i)
            if i==pivot:
                z.append(i)
            if i>pivot:
                y.append(i)
        return quicksort(x)+z+quicksort(y)
    else:
        return mylist
a=[]
print("enter the size of the list")
n=int(input())
print("enter the elements of the list")
for i in range(0,n):
    a.append(int(input()))
x=quicksort(a)
print("after sorting\n",x)
