l=list(input().split("."))
for i in range(len(l)):
    x="{0}. {1}"
    print(x.format(i+1,l[i].upper()))