"""
Implement a simple calculator that takes two numbers and an operator (+, -, *, /)
as input from the user and performs the corresponding operation. 

Bonus task if you want, it's not necessary - add degree (ხარისხი), use ** operator for it.
"""


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter an operator: ")

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
