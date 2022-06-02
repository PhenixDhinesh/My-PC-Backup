y = int(input().strip())
d=13
if y%4==0 and (y<1918 or y%400==0 or y%100!=0): d-=1
if y==1918: d+=13
print("%02d.09.%04d"%(d,y))