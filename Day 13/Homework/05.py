"""
Write a program that asks the user to enter a number between 1 and 5.
If the numberis less than 1 or greater than 5, print "Invalid input". 
If the number is between 1 and 5, print "Valid input".
"""
user_input = int(input("Please enter a number\n"))

if user_input > 5 or user_input < 5:
    print("Invalid input")
else:
    print("Valid input")