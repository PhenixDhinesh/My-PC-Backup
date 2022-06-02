n = int(input())
s = set(map(int, input().split()))
k=int(input())
for i in range(k):
    x=input()
    if x=="pop":
        s.pop()
    else:
        xx=list(x.split(" "))
        if xx[0]=="remove":
            s.remove(int(xx[1]))
        else:
            s.discard(int(xx[1]))

p=0
for i in s:
    p+=i
print(p)
