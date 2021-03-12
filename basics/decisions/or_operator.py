# Ask user for the type of adventure
print("What kind of adventure should I have?")
adv = input()

# Read user input and display message accordingly
if adv == "scary" or adv == "short":
  print("\nEntering the dark forest!")
elif adv == "safe" or adv == "long":
  print("\nTaking the safe route!")
else:
  print("\nNot sure which route to take.")