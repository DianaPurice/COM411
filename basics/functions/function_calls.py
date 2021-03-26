def run():
  # Define box function
  def box(word):
    n = 4 + len(word)
    print("-" * n)
    print("| {} |".format(word))
    print("-" * n)

  # Define lower_case function
  def lower_case(word):
    print(word.lower())

  # Define upper_case function
  def upper_case(word):
    print(word.upper())

  # Define mirrored function
  def mirrored(word):
    m = ""
    for l in reversed(word):
      m += l
      print("{} | {}".format(word, m))

  # Define repeat function
  def repeat(word):
    # Ask user how many times to repeat the word
    print("How many times should I repeat the word?")
    r = int(input())

    for d in range(r):
      # Even repetition
      if (d % 2 == 0):
        print(lower_case(word))
      # Odd repetition
      elif (d % 2 != 0):
        print(upper_case(word))
        

  # Define run function
  def run():
    print("Please enter a word:")
    word = input()

    # Create variable
    response = 0

    while (response != 6):
      print("What would you like to do with the word?")
      print("[1] Display in a box.")
      print("[2] Display in lower-case.")
      print("[3] Display in upper-case.")
      print("[4] Display mirrored.")
      print("[5] Display repeated.")
      print("[6] Quit.")

      response = int(input())

      # Determinate which function to run
      if (response == 1):
        box(word)
      elif (response == 2):
        lower_case(word)
      elif (response == 3):
        upper_case(word)
      elif (response == 4):
        mirrored(word)
      elif (response == 5):
        repeat(word)
      elif (response == 6):
        break
      else:
        print("Unkown option.")

  # Call function
  run()