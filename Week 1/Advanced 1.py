n = int(input("Enter the amount of aliens arrive on the first day: ")) #Starting aliens
x = int(input("Enter the amount of eggs each alien lays a day: ")) #Number of eggs
y = int(input("Enter the amount of days the eggs take to hatch: ")) #Days each egg takes to hatch
d = 0 #Day counter
l = int(input("Enter the amount of days: ")) #Total days

days = [0] * 34

def invade(n,l,x,y,d):
    if d == 0:
        days[d] = n
        days[d+y-1] = x * n

    days[d] = days[d] + days[d-1]
    days[d+y-1] = days[d+y-1] + days[d+y-2]
    d = d+1
    if d < l:
         return invade(n,l,x,y,d)
    else:
        return days[l-1]
    
print("The number of aliens on day " + str(l) + " is: " + str(invade(n,l,x,y,d)))
