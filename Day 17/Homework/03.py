"""
Write a function that takes a list of numbers as input and returns the largest number in the list.
"""


def largest():
    my_list = input("Please enter a number separated by spaces:\n")
    my_list = my_list.split()

    return max(my_list), min(my_list)


print(largest())


# # 2nd way
# def largest_number(numbers):
#     max_number = numbers[0]

#     for num in numbers:
#         if max_number < num:
#             max_number = num

#     return max_number


# numbers = [4, 3, 5, 2, 1]

# print(largest_number(numbers))
