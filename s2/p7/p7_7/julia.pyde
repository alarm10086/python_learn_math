from math import sqrt

xmin = -2
xmax = 2

ymin = -2
ymax = 2

rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    colorMode(HSB)
    noStroke()
    xscl = float(rangex)/width
    yscl = float(rangey)/height
    
    
def draw():
    translate(width/2,height/2)
    x = xmin
    while x < xmax:
        y = ymin
        while y < ymax:
            z = [x,y]
            c = [0.285,0.01]
            col = julia(z,c,100)
            if col == 100:
                fill(0)
            else:
                fill(3*col,255,255)
            rect(x/xscl,y/yscl,1,1)
            y += 0.01
        x += 0.01

def cAdd(a,b):
    return [a[0]+b[0],a[1]+b[1]]

def cMult(u,v):
    return [u[0]*v[0]-u[1]*v[1],u[1]*v[0]+u[0]*v[1]]

def magnitude(z):
    return sqrt(z[0]**2 + z[1]**2)

def mandelbrot(z,num):
    count=0
    z1=z
    while count <= num:
        if magnitude(z1) > 2.0:
            return count
        z1=cAdd(cMult(z1,z1),z)
        count+=1
    return num

def julia(z,c,num):
    count = 0
    z1 = z
    while count <= num:
        if magnitude(z1) > 2.0:
          return count
        z1 = cAdd(cMult(z1,z1),c)
        count += 1
    return num