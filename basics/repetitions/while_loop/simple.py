def run():
  # Ask user how many cables should beep avoid
  print("How many cables should I remove?")
  c = int(input())

  # Print blank space
  print()
  # Create variable for cables revoved
  cr = 0

  # Use a while loop to count cables removed
  while cr < c:
    print("Removed cable.")
    # increament the variable for cable removed
    cr +=1
