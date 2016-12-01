##Week 2 Question 1 Part 1. Write the pseudocode for a function which returns the highest perfect square which
##is less or equal to its parameter (a positive integer). Implement this in the programming language of your choice.

import math

def perfectSquare(n):
    print("Input number: " + str(n))
    x = math.sqrt(n)
    x = int(x)
    x = x * x
    print("Highest perfect square: " + str(x))
    return x

x = float(input("Enter a number: "))
perfectSquare(x)
