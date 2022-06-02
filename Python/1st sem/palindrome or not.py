print("enter a word")
w=input()
n=len(w)
i=0
a=[]
b=[]
while(True):
    a.append(w[i])
    i=i+1
    if(i==n):
        break
i=n-1
while(True):
    b.append(w[i])
    i=i-1
    if(i==-1):
        break
if(a==b):
    print("polindrome")
else:
    print("not a polindrome")
    
    
