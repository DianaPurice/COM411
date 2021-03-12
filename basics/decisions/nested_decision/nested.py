# Ask user for the cover type
print("Please enter the type of cover(soft/hard):")
c = input()

# Read user input and decide what to do next
if c == "soft":
  print("\nDoes the book have a perfect bound?")
  b = input()
  if b == "yes":
    print("\nSoft covered, perfect bound books are very popular!")
  else:
    print("\nSoft covers with coils or stiches are great for short books.")
elif c == "hard":
  print("\nBooks with hard covers can be more expensive!")