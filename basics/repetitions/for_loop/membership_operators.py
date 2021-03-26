def run():
  # Ask user for phrase
  print("What phrase do you see?")
  p = input()

  # Display message
  print("\nReversing phrase...", "\nThe phrase is: ", end="")

  # Create variable
  r = ""

  # Use for loop to reverse phrase
  for ph in p:
    r = ph + r

  # Display result
  print(r)