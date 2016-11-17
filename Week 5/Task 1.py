def findNextSeq(lst):
    print("Strating list: " + str(lst))
    seq = []
    l = len(lst)
    i = 1

    while i < l:
        if i != l-1:
            if lst[i] > lst[i-1] or lst[i] < lst[i+1]:
                seq.append(lst[i])
                i = i + 1
            else:
                i = i + 1
        else:
            if lst[i] > lst[i-1]:
                seq.append(lst[i])
                i = i + 1
            else:
                i = i + 1
    return seq
    
l = [12,8,7,3,7,14,10,3]
print(findNextSeq(l))
