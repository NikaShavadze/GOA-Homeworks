"""
  Create an array which will include numbers from 0 to 20 (write it manually, 
without loops), then print whole array.
"""
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(nums)

# Create a new array, which will include even numbers from the first array. Then print this new array.
nums_even = nums[::2]

print(nums_even)



"""
  Create an array, then add numbers from 50 to 100 to it. In the end, print 
the part of this array with negatives indexes.
"""
nums2 = []
for i in range(50, 101):
    nums2.append(i)
    
print(nums2[-1::-1])



"""
    Ask user for two inputs and store them as variables, their type has to be int. 
Then use for loop, use lower number from this two variables as start, Higher 
number as end, you do not need step. After that, you'll have to use if statement to only print multiples of five.
"""

user_input1 = int(input("Please enter a number: "))
user_input2 = int(input("Please enter a number: "))

my_array = []

if user_input1 > user_input2:
    my_array = [user_input2, user_input1]
    for i in range(user_input2, user_input1 + 1):
        my_array.append(i)
        if i % 5 == 0:
            print(i)
else:
    my_array = [user_input1, user_input2]
    for i in range(user_input1, user_input2 + 1):
        my_array.append(i)
        if i % 5 == 0:
            print(i)
    


"""
Create a new array. Ask user his/her age and if it will be over 18, ask 
him/her name. Then add this name to already created array and print it.
"""
my_array = []

age = int(input("Please enter your age: "))
if age >= 18:
    name = input("Please enter you name: ")
    my_array.append(name)
    print(my_array[0])