def run():
  # Ask user for phrase
  print("What phrase do you see?")
  p = input()

  # Display message
  print("\nReversing phrase...\n","\nThe phrase is: ",end="")

  # Use for loop to reverse phrase
  for ph in range(len(p) -1, -1, -1):
    print(p[ph], end="")