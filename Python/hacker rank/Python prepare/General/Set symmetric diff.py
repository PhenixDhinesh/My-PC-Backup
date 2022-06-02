n=int(input())
l=list(input().split(" "))
a=set(l[:len(l)//2])
b=set(l[len(a):])
c=a.symmetric_difference(b)
x=list(c)
print(x[0])

n=int(input())
a=set(input().split(" "))
m=int(input())
b=set(input().split(" "))
c=a.symmetric_difference(b)
l=[]
for i in c:
    l.append(int(i))
l.sort()
for i in l:
    print(i)