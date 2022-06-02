print("enter the n value")
n=int(input())
j=1
k=0
while(k<n):
    flag=0
    i=2
    j=j+1
    while(i<j):
        if(j%i==0):
            flag=1
            break
        i=i+1
    if(flag==0):
        print(j)
        k=k+1

