'''a="Dhinakaran"
for b in a:
    if b == 'a':
        continue
    if b == 'r':
        break
    print(b)

def name(x):
    x.upper()
    x*=3
    print(x)

def game(m,n):
    for z in m:
        n(z)

game(a,name)'''



'''i=9
x="asdfghjk123"
for i in x :
    print(i,end=" ")

xx=list(x)
xy=tuple(x)
print(xy)
xx.append("jai")
print(xx[4::2])
#list is immutable
dic={"a":'a',"b":'b',"c":'c',"d":'d',"d":'e'}
#do not allow duplicates
print(dic["d"])
print(dic.keys())
# normal
xxx=[]'''



'''for i in xx:
    if i!="jai":
        xxx.append(i)
print(xxx)'''



#can do like this
'''xxx=[print(i , end=' ') for i in xx if i!="jai"]
i=list(input().upper())
print(i)
u=[print(i,end=" ") for i in input() if i.isalpha()==True]
print("\n")
for i in x:
    if i.isdigit()==True:
        print(i)
'''


'''#file handling
#write or create
l=open("a.txt","w")
l.write("hai Friends")
l.close()
#read
l=open("a.txt","r")
print(l.read())
l.close()
#append
l=open("a.txt","a")
l.write("\nhai")
l.close() '''


'''l=open("a.txt","r")
f=l.readline()
print(f)
print(l.readable())
print(l.read(2))
l.close()'''


'''#for deleting file
import os
os.rename("a.txt","b.txt")
os.remove('b.txt')'''

