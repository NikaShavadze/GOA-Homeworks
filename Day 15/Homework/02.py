"""
Create a while loop that asks the user to enter a password. 
Keep asking until they enter the correct password "Goa best".
Also print the count of incorrect passwords.
"""

counter = 0
password = "Goa best"
user_input = input("Enter a password: ")

authorized = False

while authorized != True:
    if user_input == password:
        print("Access granted!")
        authorized = True
    else:
        counter += 1
        user_input = input("Enter a password: ")

print("the count of incorrect passwords", counter)
