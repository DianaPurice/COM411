def run():
  # Ask user where to Look
  print("Where should I look?")
  x = input()

  # Read in the user response and decide the next actions
  if x == "in the bedroom":
    print("\nWhere in the bedroom should I look?")
    bed = input()
    if bed == "under the bed":
      print("\nFound some shoes but no battery.")
    else:
      print("\nFound some mess but no bettery.")
  elif x == "in the bathroom":
    print("\nWhere in the bathroom should I look?")
    bat = input()
    if bat == "in the bathtub":
      print("\nFound a rubber duck but no battery.")
    else:
      print("\nFound a wet surface but no battery.")
  elif x == "in the lab":
    print("\nWhere in the lab should I look?")
    lab = input()
    if lab == "on the table":
      print("\nYes! I found my battery!")
    else:
      print("\nFound some tools but no battery.")
  else:
    print("\nI do not know where that is but I will keep looking.")