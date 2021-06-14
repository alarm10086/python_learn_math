def factors(num):
    '''返回一个由num的因数组成的列表'''
    factorList = []
    for i in range(1,num+1):
        if num % i == 0:
            factorList.append(i)
    return factorList


print(factors(120))