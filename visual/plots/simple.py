# Import pyplot
import matplotlib.pyplot as plt

# Create function display
def display(x, y):
  # Draw line
  plt.plot(x,y)
  # Display result
  plt.show()

# Create function run
def run():
  # Display message 
  print("Running...")
  # Create lists
  x_v = [1, 2, 3, 4, 5]
  y_v = [1, 4, 9, 16, 25]
  # Call the first function
  display(x_v, y_v)

# Call function run
run()