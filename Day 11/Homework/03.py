"""
    Write a program that simulates a simple login system. Ask the user for
a username and password, and if they enter "admin" and "password123", respectively, 
print "Login successful" using if-else.
"""

registered_login = "admin"
registered_password = "password123"
user_login_input = input("Login: ")
user_password_input = input("Passwprd: ")

while True:
    if user_login_input == registered_login and user_password_input == registered_password:
        print("Login successful.")
        break
    else:
        print("Incorrect password.")
        user_login_input = input("Login: ")
        user_password_input = input("Passwprd: ")