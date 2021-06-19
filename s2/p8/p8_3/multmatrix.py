def multmatrix(a,b):
    # 返回矩阵a和b的乘积
    m = len(a) # 第一个矩阵的行数
    n = len(b[0]) # 第二个矩阵的列数
    newmatrix = []
    for i in range(m):
        row = []
        # 遍历矩阵b的每一列
        for j in range(n):
            sum1 = 0
            # 对于列中的每个元素
            for k in range(len(b)):
                sum1 += a[i][k]*b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix


a = [[1,2,-3,-1]]
b = [[4,-1],
     [-2,3],
     [6,-3],
     [1,0]]

print(multmatrix(a,b))