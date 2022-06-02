g=" "
g2=g*2
g3=g*3
g4=g*4
g5=g*5
g6=g*6
g7=g*7

r="$"
r2=r*2
r3=r*3
r4=r*4
r5=r*5
r6=r*6
r7=r*7

gr=g+r
rg=r+g
s="\n"

def A():
    print(g7+s+g3+r+g3+s+g2+rg*2+g+s+gr+g3+rg+s+gr+r4+g+s+gr+g3+rg+s+gr+g3+rg+s+g7+s)
def B():
    print(g7+s+g+r4+g2+s+g+r+g3+r+g+s+g+r4+g2+s+(g+r+g3+r+g+s)*2+g+r4+g2+s+g7+s)
alphabet={'a':A,'b':B}
name=list(input().lower())
for letter in name:
    if letter=='':
        print(gr*3+g+s+rg*3+r+s)
    else:
        alphabet[letter]()
