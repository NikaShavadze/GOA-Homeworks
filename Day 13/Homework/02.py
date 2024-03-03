"""
    Write a program that asks the user to enter a number and then prints whether the
number is positive, negative, or zero using an if-else statement.
"""

number = int(input("Please enter a nummber\n"))

if number > 0:
    print("Your number is positive.")
elif number < 0:
    print("Yours number is negative.")
else:
    print("Yours number is 0.")