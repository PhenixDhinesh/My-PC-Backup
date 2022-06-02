x1,v1,x2,v2=list(map(int,input().split()))
for i in range(1,x2+1):
    if(((i*v1)+x1)==((i*v2)+x2)):
        print("YES")
        break
    elif(i==x2):
        print("NO")