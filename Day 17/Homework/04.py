"""
Write a function that takes a list of strings as input and returns 
a new list containing only the strings that start with the letter 'a'.
"""


def list_starting_with_a():
    my_list = input("Please enter a string:\n")
    my_list = my_list.split()
    filtered_list = []
    for i in my_list:
        if i.startswith("a"):
            filtered_list.append(i)
    return filtered_list


print(list_starting_with_a())
