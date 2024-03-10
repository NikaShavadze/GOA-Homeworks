"""
Write a function that checks if a given number is prime 
or not (prime number has only two divisors - გამყოფი) Use a for loop for this task.
"""

user_input = int(input("Enter a number: "))
division_counter = 0

for i in range(1, user_input + 1):
    if user_input % i == 0:
        division_counter += 1
        if division_counter == 2:
            print("Prime")
        elif division_counter == 0:
            print("Zero is neither prime nor composite")
        else:
            print("Composite")
