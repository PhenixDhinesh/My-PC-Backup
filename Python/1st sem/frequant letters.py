f=open("D:/f1.txt","r").read()
a={}
for i in f:
    if i in a:
        a[i]+=1
    else:
        a[i]=1
print(a)
