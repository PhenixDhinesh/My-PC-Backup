l = 0
v = 0
input()
for i in input():
    if i == "D": l -= 1
    else: l += 1
    
    if l == 0 and i == "U": v += 1

print(v)