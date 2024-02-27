# Write a program to display n terms of natural numbers, their sum and average
sum = 0
n = int(input("Please enter a number: "))

for i in range(1, n + 1):
    print(i)
    sum = sum + i   
average = sum / n
print("The sum is: " + str(sum))
print("The average is: " + str(average))  