'''
@Author: Smita Chichkar
@Date:  2022-04-29 17:00:00
@Last Modified by: Smita Chichkar
@Last Modified time:   2022-04-29 17:00:00
@Title :  Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
can be found using a formula
'''
import math
def  my_function(a,b,c):
     delta = (b * b - 4 * a * c)
     x1 = (-b + math.sqrt(delta)) / (2 * a)
     x2 = (-b - math.sqrt(delta)) / (2 * a)
     print(delta)
     print(x1)
     print(x2)
     
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c: "))
my_function(a,b,c)