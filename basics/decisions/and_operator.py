# Ask user what beep's seen and heard
print("What did I hear?")
s = input()
print("\nWhat did I see?")
v = input()

# Read in user's answers and decide the following actions
if s == "grrr" and v == "two red eyes":
  print("\nThere is scary creature. I should get out of here!")
else:
  print("\nI am a little scared but I will cntinue.")
