print("enter a number")
n=int(input())
i=0
if(n<10):
    print("it is a sinlge digit number")
else:
    b=n
    while(b>0):
        b=b//10
        i=i+1
print("your number is a",i,"digit one")
r=0
c=n
while(c>0):
    a=c%10
    r=r+a**i
    c=c//10
if(r==n):
    print("it is a armstrong number")
else:
    print("it is not a armstrong number")
