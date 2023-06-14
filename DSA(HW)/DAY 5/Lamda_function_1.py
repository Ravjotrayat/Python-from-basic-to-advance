#Question 2
'''
Write a python lambda expression for the following:
1. Find the modulo of two numbers and add it to the difference of the same two numbers.
2. Find the square root of a number using math library built-in function.
3. Find the square root of a number without using built-in function.
'''

#1. Find the modulo of two numbers
#   and add it to the difference of the same two numbers.
a=int(input())
b=int(input())
x=lambda a,b:a%b
dif=a-b
result = x(a,b) + dif
print("Modulo of a and b is:",x(a,b))
print("Difference of a and b is:",dif)
print("Result of modulo and difference is:",result)


#2. Find the square root of a number using math library
#   built-in function.

import math
a=int(input("\nEnter the Number for Square root"))
x=lambda a:math.sqrt(a)
print("Square Root of the Number id ",x(a))


#3. Find the square root of a number without using built-in function.
a=int(input("\nEnter the Number for Square root"))
x=lambda a:a**0.5
print("Square Root of the Number id ",x(a))
