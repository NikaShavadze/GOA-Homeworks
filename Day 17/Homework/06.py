"""
Write a function that takes a list of strings as input and returns a new list containing the lengths of each string.
"""


def string_lens_in_list():
    my_list = input("Enter a string\n")
    my_list = my_list.split()
    len_list = []
    for i in my_list:
        len_list.append(len(i))
    return len_list


print(string_lens_in_list())
