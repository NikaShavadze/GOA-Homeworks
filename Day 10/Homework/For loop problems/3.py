# Write a program to display n terms of natural numbers and their sum
sum = 0
n = int(input("Please enter a number: "))
for i in range(1, n + 1):
    print(i)
    sum = sum + i
print("The sum is: " + str(sum))