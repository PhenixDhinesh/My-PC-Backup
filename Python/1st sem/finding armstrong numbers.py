print("enter the limit (above 10)")
k=int(input())
while(k>=10):
    n=k
    i=0
    b=n
    while(b>0):
        b=b//10
        i=i+1
    r=0
    c=n
    while(c>0):
        a=c%10
        r=r+a**i
        c=c//10
    if(r==n):
        print(r)
    k=k-1
