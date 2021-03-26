# Create function short_pattern
def short_pattern():
  # Create dictionary 
  pattern = {"sequence":"101", "occurances":25}
  # Return dictionary values
  return pattern

# Create function medium_pattern  
def medium_pattern():
  # Create dictionary
  pattern = {"sequence":"111000", "ocurences":25}
  # Return dictionary values
  return pattern

# Create function long_pattern
def long_pattern():
  # Create dictionary
  pattern = {"sequence":"1100110011001100", "ocurences":50}
  # Return dictionary values
  return pattern

# Create function run
def run():
  # Display message
  print("Analysing pattern...")
  # Create dictionary
  d = {
    "short sequence": short_pattern(), 
    "medium sequence": medium_pattern(), 
    "long sequence": long_pattern()
  }
  # Create loop to display dictionary d
  for key, value in d.items():
    print(f"{key}: {value}")

# Call function run
run()
