# Ask user for nomber of rows and collums
print("How many rows should there be?")
r = int(input())
print("\nHow many collums should there be?")
c = int(input())

# Print blank
print()

# Display result
for row in range(0, r, 1):
  for col in range(0, c, 1):
    print(":-)",end="")
  print()