from turtle import *

def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

shape('turtle')
square(50)
square(30)
square()

exit()