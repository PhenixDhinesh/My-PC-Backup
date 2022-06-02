print("enter 3 positive number")
i=1
s=0
while(i<=3):
    n=int(input())
    if(n>0):
        s=s+1
        i=i+1
    elif(n<0):
        s=s-0.5
    else:
        break

print(s)
    
    
