from turtle import *

def square():
    for i in range(4):
        forward(100)
        right(90)

shape('turtle')
# speed(0)
# speed(1)
speed(10)
for i in range(60):
    square()
    right(5)

exit()

