j=list(map(int,input().split(" ")))
n=j[0]
m=j[1]
p=".|."
l=[]
for i in range(1,n,2):
    l.append((p*i).center(m,"-"))
for i in l:
    print(i)
print("WELCOME".center(m,"-"))
for i in range(len(l),0,-1):
    print(l[i-1])