'''Write a recursive function (pseudocode and code) to check if a number n is prime (hint: check whether
n is divisible by any number below n).'''

def findPrime(num, count):
    if count > (num/2): ##exits function if the count is more than half of the number
        print("Number is prime!")
        return True
    if num % count == 0: ##checks if the number/count has a remainder
        print("Number is not prime!")
        return False
    else:
        count = count + 1 ##Adds 1 to counter and calls function again
        return findPrime(num,count)


x = int(input("Enter a number: "))
findPrime(x,2)
