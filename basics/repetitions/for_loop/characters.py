def run():
  # Ask user for markings
  print("What strange marking do you see?")
  m = input()

  # Print blank
  print("\nIdentifying...\n")

  # Use for loop to display character and index of character
  for ch in range(0, len(m), 1):
    print("Index ", ch, ":", m[ch])