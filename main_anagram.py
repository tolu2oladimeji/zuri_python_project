# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    #make all characters into lower case 
    word = word.lower()
    anagram = anagram.lower()

    #check if the length of the two words are the same, continue
    #else exit the code and print not anagram
    if(len(word) == len(anagram)):

        #you need to sort the chars first
        word_sorted = sorted(word)
        anagram_sorted = sorted(anagram)

        #next compare the two sorted strings together
        if(word_sorted == anagram_sorted):
            print("True")
    else:
            print("False")
    #return True

