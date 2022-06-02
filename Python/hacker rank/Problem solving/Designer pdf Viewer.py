l=list(map(int,input().split()))
ll=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
s=input()
ss=[]
for i in s:
    ss.append(l[ll.index(i)])
print((max(ss)*len(s)))