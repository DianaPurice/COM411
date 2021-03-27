# import pyplot
import matplotlib.pyplot as plt
import csv

# create function read_data
def read_data():
  # create empty dictionary
  data = {"survives":[], "sex":[], "age":[], "fare":[]}
  # open file  
  with open("visual/subplots/titanic.csv") as file:
    # store file
    csv_reader = csv.reader(file)
    # ignore header
    header = next(csv_reader)

    # read data
    for line in csv_reader:
      survived = line[1].strip()
      sex = line[14].strip()
      age = line[4].strip()
      fare = line[8].strip()

      # create if statement to add values to the lists
      if (survived != "" and sex != "" and age != "" and fare != ""):
        data["survived"].append(bool(int(survived)))

        if (int(sex) == 0):
          data["sex"].append("male")
        else:
          data["sex"].append("female")

        data["age"].append(float(age))
        data["fare"].append(round(float(fare), 2))
      
  # return dictionary
  return data

# create function 
def plot_age_vs_survival(ax, data):
  
# create function run  
def run():
  # call and store function read data
  data = read_data()
  # Create subplots
  fig, (ax1, ax2) = plt.subplots(1, 2)
  ax1.plot(range(len(data[survived]), data[survived])
  #ax2.plot(range(len(data[age])), data[age])
  plt.show()
  #fig, ()
  #fig, ()
  #fig, ()
  
run()