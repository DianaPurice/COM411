# import pyplot
import matplotlib.pyplot as plt
# import cvs 
import csv

# reate function read_data
def read_data():
  # open file
  with open('visual/subplots/temps.csv') as file:
    # create variable
    csv_reader = csv.reader(file)
    # create empty dictionary 
    data = {'week1':[], 'week2':[]}
    # read file
    for line in csv_reader:
      # append items to lists
      data['week1'].append(float(line[0].strip()))
      data["week2"].append(float(line[1].strip()))
    # return dictionary
    return data

# create function run
def run():
  # Call and store function read_data
  data = read_data()
  
  # create subplots 
  fig, (ax1, ax2) = plt.subplots(1,2)

  # Create plots
  ax1.plot(range(len(data["week1"])), data["week1"])
  ax2.plot(range(len(data["week2"])), data["week2"])
  # display plots
  plt.show()

# Call function run
run()