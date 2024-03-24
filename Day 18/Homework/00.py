"""
შექმენით ფუნქცია, რომელსაც გადაეცემა 1-იდან 20-ის ჩათვლით რიცხვების სია. თქვენ უნდა დააბრუნოთ გაფილტრული სია, სადაც უკვე მარტო 4-ის ჯერადები იქნება.
"""


def multiplies_of_4():
    my_list = input("Please enter numbers from 1 to 20:\n")
    my_list = my_list.split()
    filtered_list = []
    for i in my_list:
        if int(i) > 0 and int(i) < 21:
            if int(i) % 4 == 0:
                filtered_list.append(i)
    return filtered_list


print(multiplies_of_4())
