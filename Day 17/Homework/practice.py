# """
# Write a function that takes a list of numbers as input and returns the product of all the numbers in the list.
# """


# def product_of_list():
#     my_list = input("Please enter numbers separated by spaces\n")
#     my_list = my_list.split()
#     product = 1
#     for i in my_list:
#         product *= int(i)
#     return product


# print(product_of_list())

# -------------------------------------------------------------------------------------------------------------

# """
# Write a function that takes a list of strings as input and returns a new
# list containing only the strings that have a length less than or equal to 3.
# """


# def less_than_3():
#     my_list = input("Please enter a string\n")
#     my_list = my_list.split()
#     filtered_list = []
#     for i in my_list:
#         if len(i) <= 3:
#             filtered_list.append(i)
#     return filtered_list


# print(less_than_3())

# -------------------------------------------------------------------------------------------------------------

# """
# Write a function that takes a list of numbers as input and returns
# a new list containing only the even numbers from the original list.
# """


# def only_evens():
#     my_list = input("Please enter numbers separated by spaces\n")
#     my_list = my_list.split()
#     filtered_list = []
#     for i in my_list:
#         if int(i) % 2 == 1:
#             filtered_list.append(i)
#     return filtered_list


# print(only_evens())

# -------------------------------------------------------------------------------------------------------------

# """
# Write a function that takes a list of numbers as input and returns the smallest number in the list.
# """

# def smallest():
#     my_list = input("Please enter numbers separated by spaces\n")
#     my_list = my_list.split()

#     return min(my_list)

# print(smallest())

# -------------------------------------------------------------------------------------------------------------

# """
# Write a function that takes a list of strings as
# input and returns a new list containing only the strings
# that end with the letter 's'.
# """


# def starting_with_s():
#     my_list = input("Please enter a string\n")
#     my_list = my_list.split()
#     filtered_list = []
#     for i in my_list:
#         if i.startswith("s"):
#             filtered_list.append(i)
#     return filtered_list


# print(starting_with_s())

# -------------------------------------------------------------------------------------------------------------

# """
# Write a function that takes a list
# of numbers as input and returns a new
# list containing the cube of each number.
# """


# def cubed_list():
#     my_list = input("Please enter some numbers separated by spaces\n")
#     my_list = my_list.split()
#     new_list = []
#     for i in my_list:
#         new_list.append(int(i) * int(i) * int(i))
#     return new_list


# print(cubed_list())

# ---------------------------------------------------------------------------------------------------------------


def evens_of_greater_than_10():
    user_input = int(input("How many numbers do you want to be in a list"))
    for i in range(user_input):
        my_list = input("enter numbers separated by spaces:\n")
    my_list = my_list.split()
    new_list = []
    for j in my_list:
        if int(j) > 10 and int(j) % 2 == 0:
            new_list.append(j)
    return new_list, sum
