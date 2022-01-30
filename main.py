from random import randint
import os

def getScore(userName):
    os.chdir('/Users/vish/Documents/Repos/BODMAS/')
    scores=dict()
    f = open('userScores.txt','r')
    for line in f:
        msg = line.split(sep=',')
        scores[msg[0]]=int(msg[1])
    f.close()
    return(scores[userName])

def updateScore(userName, score):
    newUser = True
    os.chdir('/Users/vish/Documents/Repos/BODMAS/')
    f = open('userScores.txt','r')
    scores = dict()
    for line in f:
        msg = line.split(sep=',')
        scores[msg[0]]=int(msg[1])
        newUser = newUser * True if msg[0] != userName else newUser * False
    f.close()
    if newUser == True:
        f = open('userScores.txt','a')
        f.writelines(userName + ', ' + score+'\n')
        f.close()
    else:
        scores[userName]=int(score)
        f = open('userScores.txt','w')
        for key in scores:
            line = key + ', ' + str(scores[key])
            f.writelines(line+'\n')
        f.close()
    return()

def operatorSelector():
    for i in range(4):
        operatorList.append(randint(1,3))

name = input('Please enter your name:')
print('Hello '+name)
print('Welcome to the BODMAS game')
print('Rules: First correct answer will give 10 points. Otherwise you get 5 points\n')


try:
    currentScore = getScore(name)
except: 
    currentScore = 0

print('Your current score is: '+str(currentScore))

operandList=list()
for i in range(5):
    operandList.append(randint(1,9))

operatorList=list()
operatorDict = {1:'+',2:'-',3:'*'}

operatorSelector()

expr = str(operandList[1])
for i in range(4):
    expr = expr+str(operatorDict[operatorList[i]])+str(operandList[i+1])
print('What is the value of '+expr)

first = 0
answer = False
while(answer == False):
    val = input('The answer is:')
    if str(val) == str(eval(expr)):
        print('Correct')
        answer = True
    else:
        print('Incorrect, enter the right answer')
        answer = False
        first = first+1
points = 5 if first > 0 else 10

updateScore(name,str(currentScore+points))
print('Your new score is: '+str(getScore(name)))