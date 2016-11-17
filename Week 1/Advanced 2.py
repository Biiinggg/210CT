def createMatrix(c,r):
    m = [[0 for x in range(r)] for y in range(c)]
    for x in range(c):
        for y in range(r):
            z = int(input("Enter a number: "))
            m[x][y] = z
    return m

def addMatrix(m1,m2,l):
    m3 = [[0 for x in range(l)] for y in range(l)]
    for x in range(l):
        for y in range(l):
            m3[x][y] = m1[x][y] + m2[x][y]
    print(m3)
    return m3

def subtractMatrix(m1,m2,l):
    m3 = [[0 for x in range(l)] for y in range(l)]
    for x in range(l):
        for y in range(l):
            m3[x][y] = m1[x][y] - m2[x][y]
    print(m3)
    return m3

def multiplyMatrix(m1,m2,l):
    m3 = [[0 for x in range(l)] for y in range(l)]
    for x in range(l):
        for y in range(l):
            m3[x][y] = m1[x][y] * m2[x][y]
    print(m3)
    return m3
