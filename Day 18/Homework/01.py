"""
შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლისგან 
მიღებულ სახელსა და გვარს. შემდეგ ისინი დაამატეთ სიაში და დააბრუნეთ სია.
"""


def create_a_list():
    name_surname = input("Enter your name and surname:\n")
    name_surname = name_surname.split()
    return name_surname


print(create_a_list())
