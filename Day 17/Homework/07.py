"""
Write a function that takes a list of numbers as input and 
returns the sum of all the numbers that are greater than 10.
"""


def sum_of_greater_than_10():
    my_list = input("Please enter numbers separated by space:\n")
    my_list = my_list.split()
    for i in my_list:
        if int(i) > 10:
            sum += int(i)
    return sum


print(sum_of_greater_than_10())
