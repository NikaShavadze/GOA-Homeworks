# Old, young or kid?
age = int(input("Please enter your age: "))

if age >= 50 :
    print("You are old.")
elif age >= 15 and age < 50:
    print("You are young.")
elif age < 15 and age > 0:
    print("You are a kid")
else:
    print("wrong number...")