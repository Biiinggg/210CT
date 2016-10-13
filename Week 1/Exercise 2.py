
def countZeros (n):
    if n >= 5:
        return int(countZeros(n/5) + n/5)
    else:
        return 0
inp = int(input("Enter an interger: "))
print("Number of trailing zeros: " + str(countZeros(inp)))
