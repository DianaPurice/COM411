def run():
  # Ask user for live cables to be avoided
  print("How many live cables should I avoid?")
  lc = int(input())

  # Print blank
  print()

  # Create variable to track the number of live cables avoided
  alc = 0

  # Use while operator to count how many cables have been avoided
  while alc < lc:
    print("Avoiding...", end="")
    alc +=1
    print(" Done! {} live cables avoided!".format(alc))

  # Display final message
  print("\nAll live cables have been avoided.")