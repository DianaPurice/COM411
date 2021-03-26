def run():
  # Ask user how many bars should be charged
  print("How many bars should be charged?")
  x = int(input())

  # Print blank
  print()

  # Create variable to track how many bars should be charged
  xy = 0

  # Read in user response and display the apropriate message
  while xy <= x:
    print("Charging: " + "▀ " * xy)
    xy += 1

  # Display final message
  print("\nThe battery is fully charged.")