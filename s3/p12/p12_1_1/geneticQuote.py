import random

target = "I never go back on my word, because that is my Ninja way."
characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.',?!"

# 创建和目标句字符数相同的"猜测"列表的函数
def makeList():
    '''返回一个与目标句长度相同的字符列表'''
    charList = [] # 待用随机字符填充的空列表
    for i in range(len(target)):
        charList.append(random.choice(characters))
    return charList

# 将猜测列表和目标句相比较并"打分"的函数
def score(mylist):
    '''返回一个整数：与目标句匹配的字符个数'''
    matches = 0
    for i in range(len(target)):
        if mylist[i] == target[i]:
            matches += 1
    return matches

# 随机改变一个字符使列表"变异"的函数
def mutate(mylist):
    '''返回改变了一个字符的mylist'''
    newlist = list(mylist)
    new_letter = random.choice(characters)
    index = random.randint(0,len(target)-1)
    newlist[index] = new_letter
    return newlist

# 创建一个列表，将其设为最优列表bestList
# 将最优列表的得分设为最高分bestScore
random.seed()
bestList = makeList()
bestScore = score(bestList)

guesses = 0

# 用一个无限循环创建最优列表的变种，给它评分
while True:
    guess = mutate(bestList)
    guessScore = score(guess)
    guesses += 1

    # 如果得分不比最优列表高，"继续"下一轮循环
    if guessScore <= bestScore:
        continue

    # 如果新列表拿到了满分，打印它并"跳出"循环
    print(''.join(guess),guessScore,guesses)
    if guessScore == len(target):
        break

    # 否则将新列表设为最优列表，并将它的得分设为最高分
    bestList = list(guess)
    bestScore = guessScore