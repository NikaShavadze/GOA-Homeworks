password = "12345"
guess = input("Enter the password: ")

while True:
    if guess == password:
        print("Password correct.")
        break
    else:
         print("Incorrect password.")
         guess = input("Enter the password: ")
    