# Create function observed
def observed():
  # Create empty list
  observations = []
  # Create variable to use in loop
  x = 0
  # Create loop
  while x < 7:
    # Ask user for input
    print("Please enter an observation:")
    # Store user answer
    ob = input()
    # Modify variable to decide if condition is true
    x += 1
    # Add elements to the list
    observations.append(ob)
  # Return list value
  return observations

# Create function run  
def run():
  # Display message
  print("Counting observations...")
  # Call the first function and store it localy
  observations = observed()
  # Create empty set
  o_set =set()
  # Create loop
  for o in observations:
    # Create variable to define how the data in set should be displayed
    data = (o, observations.count(o))
    # Add values to the set
    o_set.add(data)
  
  # Create loop to display set
  for data in o_set:
    print(f"{data[0]} observed {data[1]} times.")

# Call function run  
run()

