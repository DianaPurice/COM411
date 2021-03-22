# Ask user for a number
print("Please enter a number:")
n = int(input())
# Create variables to find factorial
c = 0
t = 1

# Use while loop to find the factorial
while ( c < n):
  c += 1
  t = t * c

# Display result
print("\nThe result is ",t)