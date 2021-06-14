from turtle import *

def star(sidelength):
    '''Draws a 5-pointed star of a
    given sidelength'''
    for i in range(5):
        forward(sidelength)
        right(144) #why this angle??

def starSpiral():
    '''Draws a spiral of stars'''
    length = 5
    for i in range(60):
        star(length)
        right(5)
        length += 5

shape('turtle')
speed(20)
starSpiral()

exit()