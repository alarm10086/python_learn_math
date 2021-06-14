def setup():
    size(600,600)
    rectMode(CENTER)
    colorMode(HSB)

def draw():
    background(0)
    translate(20,20)
    for x in range(20):
        for y in range(20):
            d = dist(30*x,30*y,mouseX-20,mouseY-20)
            fill(0.5*d,255,255)
            rect(30*x,30*y,25,25)