"""
    Write a program that asks the user to enter a number. If the number is
divisible by 3, print "Fizz". If the number is divisible by 5, print "Buzz". 
If the number is divisible by both 3 and 5, print "FizzBuzz". Otherwise, print the number itself.
"""

user_input = int(input("Please enter a number\n"))

if user_input % 3 == 0 and user_input % 5 == 0:
    print("FizzBuzz")
elif user_input % 5 == 0:
    print("Buzz")
elif user_input % 3 == 0:
    print("Fizz")
else:
    print(user_input)