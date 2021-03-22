# Display intital message
print("Program started!")

# Ask user for a character
print("\nPlease enter an ASCII code:")
c = int(input())

if (c in range(32,127,1)):
  print(f"\nThe character represented by the ASCII code {c} is {chr(c)}.")
else:
  print("\nThe ASCII codes should be within the range 32-126.")

# Display final message
print("\nProgram Ended!")
