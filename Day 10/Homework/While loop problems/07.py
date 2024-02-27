# Write a program to display n terms of natural numbers, their sum and average
sum = 0
n = int(input("Please enter a number: "))

i = 1
while i <= n:
    print(i)
    sum = sum + i   
    i = i + 1
average = sum / n
print("The sum is: " + str(sum))
print("The average is: " + str(average))  