from turtle import *

def square(sidelength):
    '''Draws a square of a
    given sidelength'''
    for i in range(4):
        forward(sidelength)
        right(90)

def spiral():
    length = 5
    for i in range(60):
        square(length)
        right(5)
        length += 5

shape('turtle')
speed(20)
spiral()

exit()