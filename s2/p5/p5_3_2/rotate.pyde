def setup():
    size(600,600)
    global xmin, xmax, ymin, ymax
    xmin = 0
    xmax = width
    ymin = 0
    ymax = height

def draw():
    background(255)
    translate(200, 200)
    rotate(radians(20))
    grid()
    myrect()

def myrect():
    strokeWeight(2)
    rect(20,40,50,30)

def grid():
    strokeWeight(1)
    stroke(0,255,255)
    for j in range(xmin,xmax+1):
        i = j*10
        line(i,ymin,i,ymax)
        if i > xmax+1:
            break
    for j in range(ymin,ymax+1):
        i = j*10
        line(xmin,i,xmax,i)
        if i > ymax+1:
            break
    stroke(0)
    strokeWeight(10)
    line(0,ymin,0,ymax)
    line(xmin,0,xmax,0)