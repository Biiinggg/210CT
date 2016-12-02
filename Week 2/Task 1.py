import math

def perfectSquare(n):
    print("Input number: " + str(int(n)))
    x = math.sqrt(n)##Square root
    x = int(x)##Remove decimal but converting to Int
    x = x * x##Square
    print("Highest perfect square: " + str(x))
    return x

x = float(input("Enter a number: "))
perfectSquare(x)
