# Program to print the viral of a

# k is input for number of days
# l[0] is initial value for value 5==2 (5//2)

k=int(input())
l=[2]
if k==1:print(2)
else:
    for i in range(k-1):
        l.append((l[i]*3)//2)
    print(sum(l))