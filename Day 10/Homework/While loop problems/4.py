# Write a program to display n terms of natural numbers and their sum
n = int(input("Please enter a number: "))
sum = 0

i = 1
while i <= n:
    print(i)
    i = i + 1
    sum = sum + i
print("sum: " + str(sum))