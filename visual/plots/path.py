# Import pyplot
import matplotlib.pyplot as plt

# Create function coordinate
def coordinate():
  # Promt user to input coordinates
  print("Please enter x value:")
  x = int(input())
  print("Please enter y value:")
  y = int(input())
  # Return user answer as tulip
  return (x, y)

# Create function path
def path():
  # Display message
  print("Retrieving path...")
  # Create empty lists
  x_values = []
  y_values = []
  # Create loop
  for a in range(4):
    # Call and store function coordinate
    data = coordinate()
    # Add values to the lists
    x_values.append(data[0])
    y_values.append(data[1])
  # Return lists values
  return x_values, y_values

# Create function run
def run():
  # Call and store function path
  values = path()
  # Design plot
  plt.plot(values[0], values[1], "r--o")
  # Add labels to the axes
  plt.xlabel("x values")
  plt.ylabel("y values")
  # Display plot
  plt.show()

# Call function run
run()