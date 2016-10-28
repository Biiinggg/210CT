'''Write a recursive function (pseudocode and code) that removes all vowels from a given string s. Input:
"beautiful" Output: "btfl".
'''

def removeVowels(string):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    if not string: ##Checks that there is a string
        return string
    elif string[0] in vowels:
        return removeVowels(string[1:]) ##First char is vowel so skips over it and searches the rest of word
    return string[0] + removeVowels(string[1:]) ##Returns the first character and searches the rest of the word
            
x = input("Enter a string: ")
print(removeVowels(x))
