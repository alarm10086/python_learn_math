xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangex = xmax - xmin
rangey = ymax - ymin

fmatrix = [[0, 0], [1, 0], [1, 2], [2, 2], [2, 3], [1, 3], [1, 4], [3, 4], [3, 5], [0, 5]]
transformation_matrix = [[0, -1], [1, 0]]


def setup():
    global xscl, yscl
    size(600, 600)
    xscl = width / rangex
    yscl = -height / rangey
    noFill()


def draw():
    global xscl, yscl
    background(255)
    translate(width / 2, height / 2)
    grid(xscl, yscl)

    strokeWeight(2)
    stroke(0)
    graphPoints(fmatrix)

    newmatrix = transpose(multmatrix(transformation_matrix, transpose(fmatrix)))
    stroke(255, 0, 0)
    graphPoints(newmatrix)


def grid(xscl, yscl):
    strokeWeight(1)
    stroke(0, 255, 255)
    for i in range(xmin, xmax + 1):
        line(i * xscl, ymin * yscl, i * xscl, ymax * yscl)
    for i in range(ymin, ymax + 1):
        line(xmin * xscl, i * yscl, xmax * xscl, i * yscl)
    stroke(0)
    line(0, ymin * yscl, 0, ymax * yscl)
    line(xmin * xscl, 0, xmax * xscl, 0)


def graphPoints(matrix):
    beginShape()
    for pt in matrix:
        vertex(pt[0] * xscl, pt[1] * yscl)
    endShape(CLOSE)


def addMatrices(a, b):
    C = [[a[0][0] + b[0][0], a[0][1] + b[0][1]],
         [a[1][0] + b[1][0], a[1][1] + b[1][1]]]
    return C


def multmatrix(a, b):
    m = len(a)
    n = len(b[0])
    newmatrix = []
    for i in range(m):
        row = []
        for j in range(n):
            sum1 = 0
            for k in range(len(b)):
                sum1 += a[i][k] * b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix


def transpose(a):
    output = []
    m = len(a)
    n = len(a[0])
    for i in range(n):
        output.append([])
        for j in range(m):
            # 把a[j][i]赋给output[i][j]
            output[i].append(a[j][i])
    return output