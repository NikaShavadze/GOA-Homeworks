#   Write a program that asks the user for their age and prints 
# a message based on the age range (e.g., "Child", "Teenager", 
# "Adult") using if-elif-else.

age = int(input("Please enter your age: "))

if age > 18:
    print("Adult")
elif age < 13 and age > 0:
    print("Child")
elif age < 1:
    print("Wrong number...")
else:
    print("Teenage")