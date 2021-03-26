def run():
  # Ask user for level of brigthness
  print("What level of brigthness is required?")
  b = int(input())

  # Display blank
  print()

  # Use for loop to display result
  for br in range(0, b, 2):
    print("Beep: ", "□ " * br)
    print("Bop:  ", "□ " * br)
    print()

  # Display final message
  print("\nBrigtness adjusted!")