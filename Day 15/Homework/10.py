"""
Ask user for whole number. Then create a factorial for this number and print it out 
"""

user_input = int(input("enter a number: "))
factorial = 1

if user_input != 0:
    for i in range(1, user_input + 1):
        factorial *= i
    print(factorial)
else:
    print("0")
