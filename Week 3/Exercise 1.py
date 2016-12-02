txt = input("Enter a string: ")
lst = txt.split() ##Split takes Strng input and splits up the words into List
lst.reverse() ## Reverses the order of the List
str = ' '.join(lst) ## Adds the items from the list to a String, adding a space between each entry
print(str)
