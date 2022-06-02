# a is starting of the range
# b is ending of the range
# l is last element of the list and dividing num
# o is happy days count


a,b,l=list(map(int,input().split()))
o=0
for i in range(a,b+1):
    k= (abs(i-int(str(i)[::-1]))/l)-(abs(i-int(str(i)[::-1]))//l)
    if k==0:
        o+=1
print(o)