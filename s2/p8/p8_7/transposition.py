def transpose(a):
    '''转置矩阵a'''
    output = []
    m = len(a)
    n = len(a[0])
    # 创建一个n x m的矩阵
    for i in range(n):
        output.append([])
        for j in range(m):
            # 把a[j][i]赋给output[i][j]
            output[i].append(a[j][i])
    return output