# Import pyplot
import matplotlib.pyplot as plt

# Create function small
def small():
  # Define x and y
  x = [3, 3, 4, 4, 3]
  y = [3, 4, 4, 3, 3]
  plt.plot(x, y, 'r:o')

# Create function medium
def medium():
  x = [2,2,5,5,2]
  y = [2,5,5,2,2]
  plt.plot(x, y, 'g--s')

# Create function large
def large():
  x = [1, 1, 6, 6, 1]
  y = [1, 6, 6, 1, 1]
  plt.plot(x, y, 'b-p')

# Create function run
def run():
  small()
  medium()
  large()
  plt.show()

run()