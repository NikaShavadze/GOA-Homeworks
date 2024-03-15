"""
Write a function that takes a list of numbers as input and returns the sum of all the numbers in the list.
"""


def sum_of_list():
    nums = input("enter a nums separaated by spaces")
    nums = nums.split(" ")
    sum = 0
    for i in nums:
        sum += int(i)
    print(sum)


sum_of_list()
