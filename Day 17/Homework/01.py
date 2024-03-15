"""
Write a function that takes a list of strings as input and returns a 
new list containing only the strings that have a length greater than 5.
"""


def list_of_string():
    user_input = input("Please enter a sentence\n")
    user_input = user_input.split(" ")
    filtered_list = []
    for i in user_input:
        if len(i) > 5:
            filtered_list.append(i)
    print(filtered_list)


list_of_string()
