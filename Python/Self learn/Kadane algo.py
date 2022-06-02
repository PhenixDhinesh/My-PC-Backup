s=input("Enter input : \n")
i,temp,b=0,0,''
while(i<len(s)):
    if s[i].isalpha():
        b=s[i]
        i+=1
    else:
        temp=i
        while(i!=len(s)-1 and s[i+1].isdigit()):i+=1
        print(b*int(s[temp:i+1]),end="")
        i+=1