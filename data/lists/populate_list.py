# Define function directions
def directions():
  # Create list directions
  directions = ["Move Foward", "Move Backward", "Move Left", "Move Right"]
  # Return value
  return directions

# Define function menu
def menu():
  # Display message
  print("Please select a direction:")
  # Call function directions
  d = directions()
  # Use a for loop to display obtions
  for i in range(len(d)):
    print("{}: {}".format(i, d[i]))
  # Read in user response
  i = int(input())
  # Return user response
  return d[i]

# Define function run
def run():
  # Create list route
  route = []
  # Display message
  print("Working out escape route...")
  # Use for loop to call menu function and return direction to list route 
  for count in range(5):
    route.append(menu())
  # Display message
  print(f"Escape route: {route}")
# Call function run
run()