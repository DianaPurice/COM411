# Create function likelihood
def likelihood():
  # Create tuple
  likelihoods = (50, 38, 27, 99, 4)
  # Return min and max values
  return min(likelihoods), max(likelihoods)

# Create function run
def run():
  # Call and store first function
  x = likelihood()
  # Display message
  print(f"The minimum likelihood of failing: {x[0]}%.")
  print("The maximum likelihood of failing: {}%.".format(x[1]))

  # Call function
run()