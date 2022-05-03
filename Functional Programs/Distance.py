'''
@Author: Smita Chichkar
@Date: 2022-04-29 15:00:00
@Last Modified by: Smita Chichkar
@Last Modified time:   2022-04-29 15:00:00
@Title :  Write a program Distance.py that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
'''
import math

def findDistance(x,y):
    Length = math.sqrt( math.pow(x, 2) + math.pow(y, 2))
    print("The Euclidean distance from the point ({},{}) to origin is {}".format(x,y,Length))

x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))
findDistance(x,y)