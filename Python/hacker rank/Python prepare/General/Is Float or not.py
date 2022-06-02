for i in range(int(input())):
    n=input()
    if n=="0":
        print(False)
    else:
        try:
            m=float(n)
            print(isinstance(m,float))
        except:
            print(False)