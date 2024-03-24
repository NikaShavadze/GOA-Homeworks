"""
შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. 
თქვენ უნდა დააბრუნოთ ამ სიის საშუალო არითმეტიკული ( ჯამი / სიგრძე )
"""


def my_func():
    user_input = input("Please enter numbers separated by spaces")
    my_list = user_input.split()
    sum = 0

    for i in my_list:
        sum = sum + int(i)

    average = sum / len(my_list)
    length = len(my_list)

    return average, sum, length


print(my_func())
