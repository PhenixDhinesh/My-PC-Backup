f=open("D:/f1.txt","r").read()
a=[]
for i in f:
    if i not in a:
        a.append(i)
for i in range(0,len(a)):
    print(a[i])
