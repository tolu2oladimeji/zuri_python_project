#python

Name = input("Hello, pls enter your name: ")
print("Hi ", Name)

#The user enters the text
print("Please enter a given text.\n Let it be as longggg as you want....\n Don't worry, we can handle it,\n Bring it on!!!")
User_text = input('Pls enter the text: ')

#Recall each word is separated by a space ie ' '
#we need to initialize words to 1 not 0 
#assume we also want to know number of character in the given text

words = 1
ch = 0
for i in User_text:
    ch += 1
    if(i == ' '):
        words += 1

print(" The number of words in the text is: ", words)
print("The number of character in the given text is: ", ch)