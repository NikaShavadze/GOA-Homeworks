num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
sum = 0

for i in range (num1, num2 + 1):
    sum = sum + i
    print(i)

print("sum:", str(sum))