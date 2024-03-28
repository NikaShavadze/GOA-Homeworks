"""
Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0.


"""


def find_average(numbers):
    sum = 0
    if numbers == []:
        return 0
    else:
        for i in numbers:
            sum += i
    average = sum / len(numbers)
    return average
