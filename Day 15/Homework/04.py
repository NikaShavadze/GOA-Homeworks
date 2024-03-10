"""
Ask user for five names (use input five times). Add all of them in one list and print only first three names.
"""

input1 = input("Enter a 1st name")
input2 = input("Enter a 2nd name")
input3 = input("Enter a 3rd name")
input4 = input("Enter a 4th name")
input5 = input("Enter a 5th name")

my_list = [
    input1,
    input2,
    input3,
    input4,
    input5
]

print(my_list[:3])
