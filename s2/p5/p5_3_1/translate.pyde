
xmin = 0
xmax = 300

ymin = 0
ymax = 300

rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    xscl = width / rangex
    yscl = height / rangey

def draw():
    background(255)
    translate(width/2, height/2)
    grid()
    myrect()

def myrect():
    strokeWeight(2)
    rect(20*xscl,40*yscl,50*xscl,30*yscl)

def grid():
    strokeWeight(1)
    stroke(0,255,255)
    for j in range(xmin,xmax+1):
        i = j*10
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
        if i > xmax+1:
            break
    for j in range(ymin,ymax+1):
        i = j*10
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
        if i > ymax+1:
            break
    stroke(0)
    strokeWeight(10)
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)