def run():
  # Ask user for sequence
  print("Please enter a sequence formed of dashed and 2 markers:")
  s = input()

  # Ask UserWarning
  print("\nWhat characters are the markers?")
  m = input()

  # Display blank
  print()

  # Create variables
  m1 = -1
  m2 = -1

  # Use for loop to count number of dashes between markers
  for ch in range(0, len(s), 1):
    l = s[ch]

    if (l == m):
      if (m1 == -1):
        m1 = ch
      else:
        m2 = ch

  # Display result
  print(f"The distance between the markers is {m2 - m1 -1}.")