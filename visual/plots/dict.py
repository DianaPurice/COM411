# Import pyplot
import matplotlib.pyplot as plt
# Import random
import random as rnd

# Create function data
def data():
  # Create empty dictionary
  paths = {}
  # Ask user for the type of line
  print("What kind of line would you like?(:, -- or -)")
  line = input()
  # Ask user for the colour
  print("What colour would like?(r, g, or b)")
  colour = str(input())
  # Ask user for the marker style
  print("What kind of marker would you like?(o, s or ^)")
  marker = input()
  # Add answers to the dictionary  
  paths['line'] = line
  paths['colour'] = colour
  paths['marker'] = marker
  # Return dictionary
  return paths

# create function generate  
def generate():
  # Ask user for number of line      
  print("How many lines would you like to display?")
  an = int(input())
  # Create loop  
  for l in range(an):
    # Call and store function data
    values = data()
    # Create variable
    x = rnd.sample(range(1, 10), 5)
    y = rnd.sample(range(1, 10), 5)
    # Design format
    format = f"{values['colour']}{values['line']}{values['marker']}"
    plt.plot(x, y, format)
  # Display plot  
  plt.show()

# Create function run  
def run():
  # Display message
  print("Running...")
  # Call generate function 
  generate()
  # Display message 
  print("Done!")

# Call function run
run()