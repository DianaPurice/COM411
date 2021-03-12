# Ask user for 3 whole numbers
print("Please enter the first number:")
n1 = int(input())
print("\nPlease enter the second number:")
n2 = int(input())
print("\nPlease enter the third number:")
n3 = int(input())

# Create 2 variables for odd and even numbers
odd = 0
even = 0
# Decide how many numbers are odd and how many are even
if n1 % 2 == 0:
  even +=1
else:
  odd +=1
if n2 % 2 == 0:
  even +=1
else:
  odd +=1
if n3 %2 == 0:
  even +=1
else:
  odd +=1

# Display results
print("\nThere are {} even and {} odd numbers!".format(even,odd))
