n=int(input())
s=input()
vn=0
temp=1
for i in s:
    if temp>=1:
        if i=="U":temp+=1
        else:temp-=1
    elif temp<1:
        if i=="U":temp+=1
        else:temp-=1
        if temp==1:vn+=1
print(vn)