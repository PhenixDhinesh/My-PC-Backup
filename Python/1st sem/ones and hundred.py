print("enter a number above 100")
n=int(input())
if(n<=100):
    print("enter a higher value")
else:
    a=n
    i=0
    while(a>0):
        a=a//10
        i=i+1
b=n
e=0
t=0
while(b>0):
    z=b%10
    if(i%2!=0):
        e=e+z
    else:
        t=t+z
    b=b//10
    i=i-1
print(e)
print(t)
        
            
        
        
