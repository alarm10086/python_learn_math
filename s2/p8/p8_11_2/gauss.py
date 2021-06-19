def gauss(A):
    '''通过高斯消元法将矩阵变换为一个相同的矩阵，但其最后一列包含方程组的解'''
    m = len(A)
    n = len(A[0])
    for j,row in enumerate(A):
        # 将行中元素除以对角线项
        # 将对角线项化为1
        if row[j] != 0: # 对角线项不能为0
            divisor = row[j]
            for i, term in enumerate(row):
                row[i] = term / divisor
        # 对于每行，将其他行
        # 与加法逆元相加
        for i in range(m):
            if i != j: # 对第j行不做此操作
                # 计算加法逆元
                addinv = -1*A[i][j]
                # 对于第i行的每一项
                for ind in range(n):
                    # 将第j行的对应项
                    # 乘以加法逆元
                    # 再加到第i行的这一项上
                    A[i][ind] += addinv*A[j][ind]
    return A

B = [[2,1,-1,8],
     [-3,-1,2,-1],
     [-2,1,2,-3]]
print(gauss(B))