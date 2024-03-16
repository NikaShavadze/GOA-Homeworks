"""
Write a function that takes a list of numbers as input and returns the largest number in the list.
"""


def largest():
    my_list = input("Please enter a number separated by spaces:\n")
    my_list = my_list.split()
    return max(my_list)


print(largest())
