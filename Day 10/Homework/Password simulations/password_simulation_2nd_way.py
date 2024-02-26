password = "12345"
user_enter = input("Enter the password: ")

while True:
    if user_enter == password:
        print("Access Granted!")
        break
    else:
         print("Incorrect password.")
         user_enter = input("Enter the password: ")