'''
@Author: Smita Chichkar
@Date: 2022-04-29 17:00:00
@Last Modified by: Smita Chichkar
@Last Modified time:  2022-04-29 17:00:00
@Title :  Write a program WindChill.java that takes two double command-line arguments t
and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
National Weather Service defines the effective temperature
'''
import math
import sys
def wind(t,v) :
    if(t>50 or v>120 or v<3) :
        print("Please enter the correct values in the correct ranges")
    else :
        w = (35.74 + (0.625*t) + ((0.4275*t) -35.75) * (math.pow(v,0.16)))
    print("Windspeed is {}".format(w))

t = int(input("Enter value of t : "))
v = int(input("Enter value of v : "))
wind(t,v)
