'''
@Author: Smita Chichkar
@Date:  2022-04-28 09:00:00
@Last Modified by: Smita Chichkar
@Last Modified time:   2022-04-28 09:00:00
@Title :  User Input and Replace String Template “Hello <<UserName>>, How are you?
'''
name = input("Enter your name : ")
str = "Hello {}, How are you?"
a = len(name)
b = 3
if a > b:
  print(str.format(name))
else :
   print("Please enter valid name")
