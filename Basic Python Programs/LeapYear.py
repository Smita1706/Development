'''
@Author: Smita Chichkar
@Date: 2022-04-28 07:00:00
@Last Modified by: Smita Chichkar
@Last Modified time:   2022-04-28 07:00:00
@Title :  Print the year is a Leap Year or not.
'''
year = int(input("Enter the Year to be checked: "))

if year < 1000:
    print("Please enter valid year")
elif (year%400 == 0):
          print("%d is a Leap Year" %year)
elif (year%100 == 0):                                                         
          print("%d is Not the Leap Year" %year)
elif (year%4 == 0):
          print("%d is a Leap Year" %year)
else:
          print("%d is Not the Leap Year" %year)