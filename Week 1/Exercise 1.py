import random

def shuffle(l):
    m = []
    while len(l) > 0:
        r = random.randrange(0,len(l))
        m.append(l.pop(r))
    return m

l = []
s = int(input("Enter the length of the list you want to shuffle: "))
while len(l) < s:
    x = int(input("Enter a number: "))
    l.append(x)
print("Starting list: " + str(l))
print("Shuffled list: " + str(shuffle(l)))
