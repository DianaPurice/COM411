def run():
  # Ask user for a whole number
  print("Please enter a whole number:")
  n = int(input())

  # Determinate if the number is even or odd
  if (n % 2 == 0):
    print("\nThe number {} is an even number!".format(n))
  else:
    print("\nThe number {} is an odd number!".format(n))
