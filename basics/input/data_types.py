def run():
  # Ask user for his/hers details
  print("What is your name human?")
  name = input()
  print("\nHow old are you in years {}?".format(name))
  age = int(input())
  print("\nWhat is wieght in kilograms {}?".format(name))
  weight = float(input())
  print("\nWhat is your height in meters {}?".format(name))
  height = float(input())

  # Create variable to calculate bmi
  bmi = weight / (height** 2)

  # Display message with user bmi
  print("\n{} you are {} years old and your BMI is {:.2f}".format(name,age,bmi))


