'''
@Author: Smita Chichkar
@Date: 2022-05-01 17:00:00
@Last Modified by: Smita Chichkar
@Last Modified time:  2022-05-01 17:00:00
@Title :  Flip Coin and print percentage of Heads and Tails
'''
import random

def flipCoin(N):
    TCounter = 0
    HCounter = 0
    Tpercent = 0
    Hpercent = 0
    for x in range (0,N) :
        Flip = random.random()
        print(Flip)
        if(float(Flip) < 0.5):
            TCounter += 1
        else:
            HCounter += 1
    Tpercent = (TCounter/N) * 100
    Hpercent = (HCounter/N) * 100
    print("Percentage of tail over head is {}".format(Tpercent))
    print("Percentage of head over tail is {}".format(Hpercent))
N = int(input("Enter the number to flip coin :"))
flipCoin(N)
