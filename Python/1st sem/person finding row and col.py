print("enter number of rows")
r=int(input())
print("enter number of coulmns")
c=int(input())
print("enter person number to be searched")
p=int(input())
n=r*c
if(p>n):
    print("sorry there is no one like that")
i=1
a=1
b=1
while(p>=i):
    if(p==i):
        print("coulmn number",a)
        print("row number",b)
        break
    else:
        a=a+1
        i=i+1
        if(a>r):
            a=1
            b=b+1
    
    
