from turtle import *

def polygon(sides):
    for i in range(sides):
        forward(100)
        right(360/sides)

shape('turtle')
polygon(8)

exit()