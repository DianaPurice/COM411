def run():
  # Define function escape_by
  def escape_by(plan):
    # Decide what message to display
    if (plan == "jumping over"):
      print("\nWe cannot escape that way! The boulder is too big!")
    elif(plan == "running around"):
      print("\nWe cannot escape that way! The boulder is moving too fast!")
    elif(plan == "going deeper"):
      print("\nThat might just work! Let's go deeper!")
    else:
      print("\nWe cannot escape that way! The boulder is in the way!")

  # Call function
  escape_by("jumping over")
  escape_by("running around")
  escape_by("going deeper")