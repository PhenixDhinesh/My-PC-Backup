a=[]
o=int(input("Enter list size"))
for i in range(o) :
    a.append(i)
print(a)

aa=a.index(int(input("Enter First value")))
bb=a.index(int(input("Enter second value")))
if aa==bb-1:
    print(a[bb+1:])
