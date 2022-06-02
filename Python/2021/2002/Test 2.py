a=["1","2","3","4","5"]
aa=[1,2,3,4]
def call():
    ee=int(input("Enter \"1\" For Adding New Book\nEnter \"2\" For Return Book\nEnter \"3\" For Buying Book\nEnter \"4\" For List of books\n"))
    if ee not in aa:
        print("out of options")
    else:
        if ee==4:
            print(a)
        elif ee==1 or ee==2 :
            a.append(input("Enter Book name\n"))
        elif ee==3:
            o=input("Enter Book Name\n")
            if o not in a :
                print("Book Is not avail")
            else:
                a.remove(o)
                print("Available Books List",a)
    call()
call()
    