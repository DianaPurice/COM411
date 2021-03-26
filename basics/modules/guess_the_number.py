# Import random module
import random
def run():
  # Ask user for minimum and maximum value
  print("Please enter the minimum value:")
  min = int(input())
  print("Print enter the maximum value:")
  max = int(input())

  # Create variable to represent the random number
  r = random.randrange(min, max)

  # Display message
  print(f"\nI am thinking of a number between {min} and {max}. Can you guess what it is?")

  g = 0

  while (g != r):
    print("\nPlease enter a number:")
    g = int(input())

    if (g == r):
      print("\nCongratulations!")
      break
    elif(g < r):
      print("\nYour guess is too low!")
    else:
      print("\nYour guess is too high!")

  print("\nGame Over!")
