'''Adapt the binary search algorithm so that instead of outputting whether a specific value was found, it
outputs whether a value within an interval (specified by you) was found. Write the pseudocode and
code and give the time complexity of the algorithm using the Big O notation.'''

def binarySearch(lst, low, high):
    min = 0 
    max = len(lst)-1
    middle = (min + max)/2
    while min <= max:
        middle = (min + max)//2
        if lst[middle] >= low and lst[middle]<= high: ##Return true if middle of list is within range
            return True
        if lst[middle] >= low and lst[middle] >= high:
            max = middle - 1 ##Reduce middle if value is greater than range
        else:
            min = middle + 1 ##Increase middle is value is smaller than range
    return False ##Value not in range
        

l = [1,3,6,7,11,15,17]
print(binarySearch(l,11,13))
