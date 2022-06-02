from turtle import *

color('black', 'lightgreen')
begin_fill()
while True:
    backward(200)
    right(50)
    if abs(pos()) < 1:
        break
end_fill()
done()
