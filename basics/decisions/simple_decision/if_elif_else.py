def run():
  # Ask user for direction to paint
  print("Towards which direction should I paint?")
  d = input()
  print()

  # Use if/elif/else to determinate the direction
  if d == "up":
    print("\nI am painting in the upward direction!")
  elif d == "down":
    print("\nI am painting in the downward direction!")
  elif d == "left":
    print("\nI am painting in the leftward direction!")
  elif d == "right":
    print("\nI am painting in the rightward direction!")
  else:
    print("\nI do not understand this direction!")
  # Print final message
  print("\nI finnished painting!")