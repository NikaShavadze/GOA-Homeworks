"""
    დავალება: შექმენით პროგრამა, სადაც მომხმარებელს შემოატანინებთ თუ რამდენ რიცხვს 
შეიტანენ სიაში. შემდეგ შექმენით სია, for ციკლში input-ით შეეკითხეთ რიცხვი და შეიტანეთ 
ამ სიაში ეს რიცხვები. ბოლოს სიის ჯამი დააბრუნეთ
    დავალების შემდეგი ნაწილი: გაფილტრეთ სია ისე, რომ დაბრუნდეს 10-ზე მეტი ლუწი რიცხვები
"""


def evens_of_greater_than_10():
    user_input = int(input("How many numbers do you want to be in a list\n"))
    new_list = []
    for i in range(user_input):
        my_list = input("enter numbers separated by spaces:\n")
        my_list.append(i)
    my_list = my_list.split()
    for j in my_list:
        if int(j) > 10 and int(j) % 2 == 0:
            new_list.append(j)
    return new_list, sum


print(evens_of_greater_than_10())
