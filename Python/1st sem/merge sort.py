def mergesort(mylist):
    if(len(mylist)<2):
       return mylist
    mid=len(mylist)//2
    x=mergesort(mylist[:mid])
    y=mergesort(mylist[mid:])
    output=[]
    i=0
    j=0
    while(i<len(x) and j<len(y)):
        if(x[i]>y[j]):
            output.append(y[j])
            j+=1
        else:
            output.append(x[i])
            i+=1
    output+=x[i:]
    output+=y[j:]
    return output
a=[]
print("enter the size of the list")
n=int(input())
print("enter the elements of the list")
for i in range(0,n):
    a.append(int(input()))
x=mergesort(a)
print("after sorting\n",x)
