"""
    Write a program that simulates a basic ATM. It should ask the user for their PIN, 
and if it's correct, display a text withdrawal, deposit, and balance.
"""

registered_password = "1234"
user_input = input("Please enter your PIN: ")

while True:
    if user_input == registered_password:
        print("Withdrawal")
        print("Deposit")
        print("Balance")
        break
    else:
        print("Password incorrect.")
        user_input = input("Please enter your PIN: ")
    