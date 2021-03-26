def run():
  # Display initial message
  print("Program started!")

  # Ask user for a character
  print("Please enter a character:")
  c = input()

  if (len(c) == 1):
    print(f"\nThe ascii code of {c} is {ord(c)}")
  else:
    print("\nAsingle character was expected.")

  # Display final message
  print("\nProgram ended!")