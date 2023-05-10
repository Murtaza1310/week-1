#Q5. Using a while loop, verify if the number A is purely divisible by number B and if so then how many 
#times it can be divisible.

# Take input values for A and B
A = int(input("Enter a value for A: "))
B = int(input("Enter a value for B: "))

# Initialize count to zero
count = 0

# Use a while loop to check if A is divisible by B
while A % B == 0:
    A = A / B
    count += 1

# Check if count is greater than zero
if count > 0:
    print("A is divisible by B ", count, " times.")
else:
    print("A is not divisible by B.")
