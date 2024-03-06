# 1st way
password = "12345"
user_enter = input("Please enter a password")

while user_enter != password:
    print("Incorrect password.")
    user_enter = input("Please enter a password")
print("Access Granted!")

# 2nd way
password = "12345"
user_enter = input("Enter the password: ")

while True:
    if user_enter == password:
        print("Access Granted!")
        break
    else:
         print("Incorrect password.")
         user_enter = input("Enter the password: ")