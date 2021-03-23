# Define function movements
def movements():
  # Create list path
  path = ["Move Foward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
  # Return list path
  return path

# Define function run
def run():
  # Display message
  print("Moving...")
  # Call the fist function and store it in a local variable
  path = movements()
  # Display message
  print(path[0], "for", path[1], "steps")
  print(f"{path[2]} for {path[3]} steps")
  print("{} for {} steps".format(path[4],path[5]))
  print(f"{path[6]}" + " for " + "{}".format(path[7]) + " steps")

# Call function run
run()
