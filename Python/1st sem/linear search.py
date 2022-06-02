def linear(a,f):
    pos=-1
    for i in range(0,len(a)):
        if(a[i]==f):
            pos=i
            print("element present in position",pos+1
                  )
            break
    if(pos==-1):
        print("element is not present in the list")
    return
a=[]
print("enter the size of the list")
n=int(input())
print("enter the elements of the list")
for i in range(0,n):
    a.append(int(input()))
print("enter element to find in the list")
find=int(input())
linear(a,find)
                  
    
