print("ENTER YOUR GUESS (WITHIN 1000)")


a=156
i=6
while(True):
    b=int(input())
    if(a==b):
        print("correct")
        break
    elif(i==1):
        print("sorry you don't have chance more")
        break
    elif(a<b):
        print("low one")
        i=i-1
        print("you have",i,"chances left")
    elif(a>b):
        print("greater one")
        i=i-1
        print("you have",i,"chances left")
    
    
        
