# Import pyplot
import matplotlib.pyplot as plt

# Create function read_data
def read_data(file_path):
  # Create empty list to store data from file
  temps = []
  # Open file
  with open(file_path) as file:
    # Create loop to read file
    for line in file:
      # Append items from file to list
      temps.append(float(line.strip()))
  # Return list
  return temps

# Create function run
def run():
  # Call the first function and store it
  data = read_data("visual/subplots/temps.txt")
  # create subplots
  fig, (ax1, ax2) = plt.subplots(1, 2)
  # 
  ax1.plot(range(len(data)), data)
  ax2.bar(range(len(data)), data)
  # Display plot
  plt.show()

# Call function run
run()