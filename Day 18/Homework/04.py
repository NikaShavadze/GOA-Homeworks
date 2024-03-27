"""
შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლის გვარს.
გვარის თითოეული ასო გადაიტანეთ ახალ სიაში. შემდეგ for ციკლის გამოყენებით
იმუშავეთ ამ სიაზე - მარტო ლუწ ინდექსებზე მყოფი ასოები დაამატეთ ახალ სიაში.
საბოლოოდ დააბრუნეთ ეს სია.

Bonus (არაა სავალდებულო): ეს სია გარდაქმენით სთრინგად და ამ სახით დააბრუნეთ
"""


def even_indexes():
    user_input = input("Please enter your surname: ")
    my_list = []

    for index in range(len(user_input)):
        if index % 2 == 0:
            my_list.append(user_input[index])

    return my_list


print(even_indexes())
