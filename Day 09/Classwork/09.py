# 1st way
# password = "12345"
# enter = input("Please enter a password")
# while enter != password:
#     enter = input("Please enter a password")
# print("Access Granted!")

# 2nd way
password = "12345"
guess = input("Enter the password: ")

while True:
    if guess == password:
        print("Password correct.")
        break
    else:
         print("Incorrect password.")
         guess = input("Enter the password: ")