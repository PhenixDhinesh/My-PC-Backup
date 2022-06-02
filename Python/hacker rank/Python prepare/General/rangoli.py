l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
n=int(input("Enter the size of the Rangoli:"))
ts=(n+(n-1))*2 - 1
t=(ts//2)+1
ll=l[0:n]
ll.sort(reverse=True)
l3=[]
for i in range(n):
    k="-".join(ll[:i+1])
    kk=k.rjust(t,"-")
    rv=kk[::-1]
    l3.append(kk+rv[1:])
for i in range(n):
    print(l3[i])
l3.sort(reverse=True)
for i in range(n-1):
    print(l3[i+1])
    