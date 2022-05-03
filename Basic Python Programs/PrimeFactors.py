'''
@Author: Smita Chichkar
@Date: 2022-04-29 17:00:00
@Last Modified by: Smita Chichkar
@Last Modified time:  2022-04-29 17:00:00
@Title :  Computes the prime factorization of N using brute force.

'''
def calculate_prime_factors(Number):
   i = 1
   while(i <= Number):
    count = 0
    if(Number % i == 0):
        j = 1
        while(j <= i):
            if(i % j == 0):
                count = count + 1
            j = j + 1
            
        if (count == 2):
            print(" %d is a Prime Factor of a Given Number %d" %(i, Number))
    i = i + 111


input_number = int(input("Enter the number to find its prime factors : "))
output = calculate_prime_factors(input_number)
print("Prime factors of {} are {}".format(input_number, output))
