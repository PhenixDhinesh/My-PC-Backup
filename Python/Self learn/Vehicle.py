c=True
flag=2
while(c==True):
    print("Enter :\n1 For Start \n2 for stop\n3 for stop the program")
    k=int(input())
    if flag==k and k==1: print("The vehicle is already started")
    elif flag==k and k==2: print("The vehicle is already stoped")
    elif k==1:
        flag=k
        print("Vehicle is started")
    elif k==2:
        flag=k
        print("Vehicle is stoped")
    elif k==3:
        print("program is stoped")
        c=False