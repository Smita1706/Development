'''
@Author: Smita Chichkar
@Date: 2022-04-30 16:00:00
@Last Modified by: Smita Chichkar
@Last Modified time:  2022-05-01 17:00:00
@Title : Find Harmonic Number
'''

def harmonic(N):
    sum = 0
    if N<0 :
      print("Please enter valid number")
    for x in range(1,N+1):
        sum += 1/x
    print(sum)
N = int(input("Enter the number to find harmonic : "))
harmonic(N)