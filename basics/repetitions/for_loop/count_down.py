# Ask user for distance
print("How far are we from the cave?")
d = int(input())

# Display blank space
print()

# Display result
for ds in range(d, 0, -1):
  print(ds, "steps remaining.")

# Display final message
print("\nWe have reached the cave!")