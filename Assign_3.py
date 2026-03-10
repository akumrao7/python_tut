
# Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

inp=int(input("Enter a number: "))
print(f"The factorial of {inp} is {factorial(inp)}")

#Task 2: Using the Math Module for Calculations

import math

num = float(input("Enter a number: "))
sq=math.sqrt(num)
print(f"Square root: {sq}")

lg=math.log(num)
print(f"Logarithm: {lg}")

sin=math.sin(num)
print(f"Sin: {sin}")