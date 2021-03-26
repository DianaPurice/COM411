def run():
  # Ask user for how many numbers to be added
  print("How many numbers should I be summing?")
  nts = int(input())

  # Create variables to use while counting
  ns = 0
  t = 0

  # Use while loop to ask for the numbers and count
  while ns < nts:
    print(f"\nPlease enter number {ns} of {nts}: ")
    n = int(input())
    ns +=1
    t = t + n

  # Display result
  print(f"\nThe result is : {t}")