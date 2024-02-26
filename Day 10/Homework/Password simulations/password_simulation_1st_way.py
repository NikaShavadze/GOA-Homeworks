password = "12345"
user_enter = input("Please enter a password")

while user_enter != password:
    print("Incorrect password.")
    user_enter = input("Please enter a password")
print("Access Granted!")