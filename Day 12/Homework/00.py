#sum of the first 10 numbers
sum = 0

i = 1
while i <= 10:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
    
print(sum)