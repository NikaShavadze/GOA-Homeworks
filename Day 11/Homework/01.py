# Write a program that calculates the sum of a number entered by the user using a while loop.

n = int(input("Please enter a number: "))
sum = 0

i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print(sum)