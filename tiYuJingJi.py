#!/usr/bin/env python
#-*- coding = utf-8 -*-
from random import random
def printIntro():    #打印信息
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0-1之间的小数表示）")

def getInputs():  #获取用户输入
    a = eval(input("请输入选手A的能力值（0-1）："))
    b = eval(input("请输入选手B的能力值（0-1）："))
    n = eval(input("模拟比赛的场次："))
    return a,b,n

def simNGames(n,probA,probB):   # n 场比赛过程
    winsA,winsB = 0,0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)   #调用1 场比赛的过程
        if scoreA >scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB

def simOneGame(probA,probB):  # 1 场比赛过程
    scoreA,scoreB = 0,0
    serving = "A"
    while not gameOver(scoreA,scoreB):   #如果比赛未结束（调用比赛终止函数）
        if serving =="A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA,scoreB

def gameOver(a,b):    #比赛终止规则
    return a==15 or b==15

def printSummary(winsA,winsB):     #输出函数
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))

def main():    #调用所有函数（包括执行顺序）
    printIntro()
    probA,probB,n = getInputs()  #将用户输入的值赋给probA和proB、及模拟场次n
    winsA,winsB = simNGames(n,probA,probB)
    printSummary(winsA,winsB)

main()
