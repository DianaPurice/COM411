# Create function likelihood
def likelihood():
  # Create tuple
  likelihoods = (50, 38, 27, 99, 4)
  # Return minumum value
  return min(likelihoods)

# Create function run
def run():
  # Call and store function likelihood
  x = likelihood()
  # Display message
  print(f"Minimum likelihood of failing: {x}%.")

run()