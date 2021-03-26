# Create function observed
def observed():
  # Create empty list
  observations = []
  # Populate list with user answer
  for count in range(5):
    print("Please enter observation:")
    # Read and store user answer
    u = input()
    # Populate list
    observations.append(u)
    # Return list value
  return observations

# Create function remove_observations
def remove_observations(observations):
  # Create variable
  is_running = True
  # Create loop
  while(is_running):
    # Ask user if they want to remove an observation
    print("Would you like to remove an observation?(yes/no)")
    # Read and store user answer
    an = input()
    # Create if statement
    if (an == "yes"):
      # Ask user what he wants to remove
      print("Which observation would you like to remove?")
      # Read and store user answer
      o_r = input()
      # Remove observation
      observations.remove(o_r)
    else:
      is_running = False

# Create function run
def run():
  # Call and store the first funtion
  observations = observed()
  # Call the second function
  remove_observations(observations)
  # Create set
  o_set = set()
  # Create loop to populate set
  for o in observations:
    # Create variable to set how the data should be displayed
    data = (o, observations.count(o))
    # Populate set
    o_set.add(data)
  # Display sorted function  
  # Create loop  
  for data in sorted(o_set):
    # Display sorted list
    print(f"{data[0]} observed {data[1]} times.")

# Call fucntion run  
run()