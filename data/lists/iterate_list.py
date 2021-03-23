# Define function directions
def directions():
  directions = ["Move Foward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

# Define function menu
def menu():
  # Display message
  print("Please select a direction:")
  # Call the function direction and store it
  dirs = directions()
  # Use a for loop
  for index in range(len(dirs)):
    print(f"{index}: {dirs[index]}")

# Define function run
def run():
  menu()

# Call function run
run()