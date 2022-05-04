'''
@Author: Smita Chichkar
@Date: 2022-05-02 17:00:00
@Last Modified by: Smita Chichkar
@Last Modified time:  2022-05-01 17:00:00
@Title :  > Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.
'''
import random
def gamble(n,s,g):
    bets = 0 
    wins = 0
    for x in range(0,n):
        cash = s
        while (cash > 0 and cash < g) :
            bets += 1
            if (random.random() < 0.5):
                cash += 1
            else:
                cash -= 1
            if (cash == g):
                wins += 1
    wonPercentage = 100 * wins / n
    lossPercentage = 100 * (n - wins) / n
    print("{} wins out of of {}".format(wins,n))
    print("Percent of games won {} ".format(wonPercentage))
    print("Percent of games loss {} ".format(lossPercentage))
N = int(input("Please enter no of times to gamble :"))
stack = int(input("Please enter stack amount :"))
goal = int(input("Please enter goal amount :"))
gamble(N,stack,goal)