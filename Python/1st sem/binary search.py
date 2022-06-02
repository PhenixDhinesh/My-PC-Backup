def binary(a,search,s):
    find=False
    beg=0
    end=s-1
    while(beg<=end):
        mid=(beg+end)//2
        if(a[mid]==search):
            find=True
            print("element is present")
            break
        elif(a[mid]<search):
            beg=mid+1
        else:
            end=mid-1
        if(find==False):
            print("element is not present")
            break
a=[]
print("enter the size of the list")
s=int(input())
print("enter elements of list")
for i in range(0,s):
    a.append(int(input()))
print("enter the element to be searched")
search=int(input())
binary(a,search,s)
                  
    
