"""
Using for loop, ask user for number. Then create a list which
will have even numbers in next range: from 0 to user's number. 
At last, print out whole list. 
"""

user_input = int(input("Enter a number: "))
my_list = []

for i in range(0, user_input + 1):
    if i % 2 == 0:
        my_list.append(i)
print(my_list)
