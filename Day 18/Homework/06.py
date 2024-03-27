"""
შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან სიტყვას. შემდეგ თქვენ უნდა 
მოახდინოთ ამ სიტყვის შებრუნება, მაგ: word - drow. საბოლოდ კი დააბრუნეთ შედეგი.
"""


def reverse():
    user_input = input("Write something that you what to reverse: ")
    my_list = []

    for index in range(len(user_input), 0, -1):
        my_list.append(user_input[index])

    return my_list


print(reverse())
