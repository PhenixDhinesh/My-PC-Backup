n=int(input("enter a number\n"))
def chose(x,y):
    p=x
    a=['A','B','C','D','E','F']
    b=[]
    while(x>0):
        k=x%y
        b.append(int(k))
        x=x/y
        if(x<y):
            b.append(int(x))
            break
    print("\nthe",y,"value of",p,":")
    for i in range(len(b)-1,-1,-1):
        if(b[i]>10):
            a2=b[i]-10
            b[i]=a[a2]
        print(b[i],end='')
m=2
chose(n,m)
m=8
chose(n,m)
m=16
chose(n,m)
