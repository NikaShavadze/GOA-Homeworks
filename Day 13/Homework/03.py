"""
Write a program that asks the user to enter a password. 
If the password is "abc123", print "Access granted"; otherwise, print "Access denied".
"""

user_input = input("Please enter a password\n")
user_password = "abc123"

if user_input == user_password:
    print("Access granted/")
else:
    print("Access denied.")