class h:
    def __init__(self, h1, h2):
        self.h1 = h1
        self.h2 = h2

    def min(self):
        print(self.h2 - 1)

    def max(self):
        c = self.h2 - 4
        print(c)

        def pus():
            print(c + 20)

        pus()


hu = h("tr", 6)
print(hu.h1)
hu.max()

#lambda  single line coding instead of def like things
x=lambda a,b : a+b+int(input())
print(x(1,2))
def hh(d):
    return lambda a : a*d

k=hh(10)

print(k(12))
#map paring func to iteratbale things
def sq(x):
    return x**x
num=[1,2,3,4]
print(list(map(sq,num)))