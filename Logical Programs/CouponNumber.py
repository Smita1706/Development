'''
@Author: Smita Chichkar
@Date: 2022-05-01 17:00:00
@Last Modified by: Smita Chichkar
@Last Modified time:  2022-04-30 10:00:00
@Title :  Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.

'''
import random
def coupounNumber(cpNum):
    count=0
    for i in range(200):
        randomNum=random.randint(10,100)
        if(randomNum==cpNum):
            count+=1
    print("The Coupon Number ",cpNum," has repeated ",count," times")
cpNum =int(input("Enter a number :"))
coupounNumber(cpNum)