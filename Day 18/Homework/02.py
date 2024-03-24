"""
მომხმარებელს შეეკითხეთ საწყისი და საბოლოო რიცხვები. ეს რიცხვები გადაეცით 
ფუნქციას, for ციკლით სიაში შეინახეთ მათ შორის არსებული რიცხვები. შემდეგ მოახდინეთ 
გაფილტვრა, ისევ for ციკლით განიხილეთ თითოეული რიცხვი - თუ რიცხვი ლუწი იქნება, 
ახალ სიაში დაამატეთ მისი მეორე ხარისხი, ხოლო თუ კენტი იქნება სიაში დაამატეთ მისი 
კვადრატული ფესვი (0.5 ხარისხი).
"""


def my_func():
    num1 = int(input("Please enter a staring number: "))
    num2 = int(input("Please enter an ending number: "))
    my_list = []

    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            i = i ** 2
            my_list.append(i)
        elif i % 2 == 1:
            i = i ** 0, 5
            my_list.append(i)

    return my_list
