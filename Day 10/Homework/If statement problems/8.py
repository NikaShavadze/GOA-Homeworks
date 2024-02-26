# Is n multiple of 10?
n = int(input("Please enter a number: "))

if n % 10 == 0:
    print(str(n), "is a multiple of 10.")
else:
    print(str(n), "is not a multiple of 10.")