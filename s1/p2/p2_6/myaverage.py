
def mysum(numList):
    running_sum = 0
    for num in numList:
        running_sum += num
    return running_sum

def myaverage(numList):
    return mysum(numList)/len(numList)

d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42, 15, 96, 11, 70, 83, 97, 75]
print(myaverage(d))