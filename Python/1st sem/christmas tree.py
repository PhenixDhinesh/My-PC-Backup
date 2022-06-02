n=int(input("enter a odd number\n"))
if(n%2!=0):
    j=1
    m=n*2
    for i in range(0,n):
        k=m-j
        k1=k/2
        for l in range(0,int(k1)):
            print(" ",end='')
        for k in range(0,j):
            print("*",end='')
        print("\n")
        j=j+2
else:
    print("it is not a odd number")
