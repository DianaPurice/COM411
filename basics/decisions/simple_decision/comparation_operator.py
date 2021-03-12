# Ask user for 2 numbers
print("Please enter the first number:")
n1 = float(input())
print("\nPlease enter the second number:")
n2 = float(input())

# Determinate the relationship between the numbers
if n1 < n2:
  print("\nThe first number is the smallest!")
elif n1 > n2:
  print("\nThe second number is the smallest!")
else:
  print("\nBoth numbers are equal!")
