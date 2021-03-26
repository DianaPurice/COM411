def run():
  # Define display_ladder function
  def display_ladder(steps):
    # Display steps
    for step in range(steps):
      print("|__|")

    # Display bottom of create_ladder
    print("|  |")

  # Define create_ladder function
  def create_ladder():
    # Ask user for number of steps
    print("How many steps?")
    steps = int(input())
    display_ladder(steps)

  # Call function
  create_ladder()