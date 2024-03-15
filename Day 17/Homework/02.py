"""
Write a function that takes a list of numbers as input and returns 
a new list containing only the even numbers from the original list.
"""


def even_nums():
    user_list = input("please enter nums separated by spaces\n")
    user_list = user_list.split(" ")
    filtered_list = []
    for i in user_list:
        if int(i) % 2 == 0:
            filtered_list.append(i)
    print(filtered_list)


even_nums()
