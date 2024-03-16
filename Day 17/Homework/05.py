"""
Write a function that takes a list of numbers as input and returns a new list containing the square of each number.
"""


def squared_list():
    my_list = input("Please enter numbers separated by space\n")
    my_list = my_list.split()
    new_list = []
    for i in my_list:
        new_list.append(int(i) * int(i))
    return new_list


print(squared_list())
