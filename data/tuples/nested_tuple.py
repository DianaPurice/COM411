# Create funtion steps
def steps():
  likelihood = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
  # Return value
  return likelihood

# Create function run
def run():
  # Call function steps and store it
  x = steps()
  # Create 2 empty lists
  good_steps = []
  bad_steps = []
  # Create loop
  for step in x:
    if (step[1] >= 50):
      bad_steps.append(step)
    else:
      good_steps.append(step)
  # Display bad and good steps
  print(f"Good steps: {len(good_steps)}. \nBad steps: {len(bad_steps)}.")

# Call function run
run()