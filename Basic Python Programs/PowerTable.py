'''
@Author: Smita Chichkar
@Date: 2022-04-30 17:00:00
@Last Modified by: Smita Chichkar
@Last Modified time: 2022-04-30 17:00:00
@Title :  Print power table of 2
'''
def table(N):
    i = 0
    base = 2
    power = 1
    if(N>0 and N<31):
      while(i<N):
        power = power * base
        print(power)
        i=i+1
    else :
          print("Please enter value between 0 to 31")

table(10)