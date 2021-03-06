def setup():
    size(600,600)
    noStroke()

def draw():
    background(255)
    translate(width/2,height/2)
    points = []
    t = 0
    while t < 1000:
        points.append(harmonograph(t))
        t += 0.01
    
    for i,p in enumerate(points):
        stroke(0)
        if i < len(points) - 1:
            line(p[0],p[1],points[i+1][0],points[i+1][1])

def harmonograph(t):
    a1,a2 = 100,200
    f1,f2 = 1,2
    p1,p2 = 0,PI/2
    d1,d2 = 0.02,0.02
    x = a1*cos(f1*t + p1)*exp(-d1*t)
    y = a2*cos(f2*t + p2)*exp(-d2*t)
    return [x,y]