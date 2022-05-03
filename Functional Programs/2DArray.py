'''
@Author: Smita Chichkar
@Date: 2022-05-01 14:00:00
@Last Modified by: Smita Chichkar
@Last Modified time:  2022-05-01 17:00:00
@Title :  A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.

'''
import array

def printArray(r,c):
    arr = []
    for i in range(r):
        col = []
        for j in range(c):
            col.append(int(input("Enter the number : ")))
        arr.append(col)
    print(arr)
R = int(input("Enter the number of rows : "))
C = int(input("Enter the number of rows : "))
printArray(R,C)