"""
    შექმენით მასივი, for ციკლით მასივში დაამატეთ 0-იდან 50-ის
ჩათვლით რიცხვები. შემდეგ 0-იდან 25-ე ინდექსის ჩათვლით გამოიტანეთ რიცხვები.
"""

my_list = []

for i in range(50+1):
    my_list.append(i)
print(my_list[:25+1])


"""
 მომხმარებელს შეეკითხეთ რიცხვი. შემდეგ for ციკლით  start პოზიციად ეს რიცხვი,
 ხოლო end-ად ამ რიცხვზე ათით მეტი აიღეთ და ყველა რიცხვი ჩაამატეთ ახალ სიაში
 . სიიდან გამოიტანეთ ელემენტები 2 ინდექსის გამოტოვებით
"""

my_list = []
start = int(input("Enter a number: "))
end = start + 10

for i in range(start, end + 1):
    my_list.append(i)
print(my_list[::2])
