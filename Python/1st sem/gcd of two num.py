a=int(input())
b=int(input())
if(a<b):
    min=a
else:
    min=b
while(min>=1):
    if(a%min==0 and b%min==0):
        print("GCD is ",min)
        break
    min=min-1
