# Write a program to compute the sum of the first 10 natural numbers.
sum = 0
for i in range(1, 11):
    print(i)
    sum = sum + i
print("The sum is: " + str(sum))