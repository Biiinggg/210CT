def findNextSeq(lst):
    print("Starting list: " + str(lst))

    currentLst = []##List for the subsequence currently iterating over
    biggestLst = []##Lst for sotring the biggest subsequence so far
        
    for x in range(0, len(lst)): ##For all items in list
        current = lst[x]##Current value of list
        previous = lst[x-1]##Previous value of list
        if current > previous:##if current is bigger than previous
            currentLst.append(current)##add to the list
        elif len(currentLst) > len(biggestLst):##if current list is bigger than bigest list
            biggestLst = currentLst
            currentLst = [current]
        else:
            currentLst = [current]
    if len(biggestLst) < len(currentLst):
        return currentLst
    return biggestLst

l = [1,3,8,5,9,11,13,2,5,7]
print("Longest Subsequence: " + str(findNextSeq(l)))
