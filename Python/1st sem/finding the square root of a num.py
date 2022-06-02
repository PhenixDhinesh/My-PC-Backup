def square(num):
    approx=0.5*num
    better=0.5*(approx+(num/approx))
    while(better!=approx):
        approx=better
        bettrer=0.5*(approx+(num/approx))
    return approx
print("enter the number")
num=int(input())
res=square(num)
print("square root",num,"is",round(res,3))
