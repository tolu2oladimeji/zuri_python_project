#python
#This is a simple calculation
#User writes names
Name = input('Enter your name: ')
print("Hi ", Name)

#Enter two numbers for calculation

First_Number= float(input("Enter first number"))
Second_Number = float(input("Enter Second number"))

# pick an option
print("What will you like to do?")
print("Enter: \n1 for addition\n 2 for subtraction\n 3 for division\n 4 for multiplication\n 5 for modulus operations\n 6 All Calculation")
Selected_Option = int(input("Enter Option: "))

#Declare storing variables

Add_Number = 0.00
Subtract_Number = 0.00;
Divide_Number = 0.00;
Multiply_Number =0.00;
Mod_Number = 0.00;

#All calculations goes here
Add_Number = First_Number + Second_Number
Subtract_Number = First_Number - Second_Number
Divide_Number = First_Number / Second_Number
Multiply_Number = First_Number * Second_Number
Mod_Number = First_Number % Second_Number


if Selected_Option == 1:
    print("The addition of the numbers is: ", Add_Number)

elif Selected_Option == 2:
    print("The Subtraction of the numbers is: ", Subtract_Number)

elif Selected_Option == 3:
    print("The Division of the numbers is: ", Divide_Number)

elif Selected_Option == 4:
    print("The Multiplication of the numbers is: ", Multiply_Number)

elif Selected_Option ==5:
    print("The modulus operation of the numbers is : ", Mod_Number)

elif Selected_Option == 6:
    print("You asked for all calculations")
    print("The addition of the numbers is: ", Add_Number)
    print("The Subtraction of the numbers is: ", Subtract_Number)
    print("The Division of the numbers is: ", Divide_Number)
    print("The Multiplication of the numbers is: ", Multiply_Number)
    print("The modulus operation of the numbers is : ", Mod_Number)

else:
    print("Select an Option")

    





