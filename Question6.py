#Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is 
#divisible by 3 or not.

# Create a list of 25 integers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# Check if each element in the list is divisible by 3 or not using a for loop
for num in nums:
    if num % 3 == 0:
        print(num, "is divisible by 3")
    else:
        print(num, "is not divisible by 3")
   
 