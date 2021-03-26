def run():
  # Define function sum_weights
  def sum_weights(beep, bop):
    w = beep + bop
    return w

  # Define calc_avg_wieght
  def calc_avg_weight(beep, bop):
    a_w = (beep + bop)/2
    return a_w

  # Define function run
  def run():
    #Ask user for each robot weight
    print("Please enter Beep's weight:")
    beep = float(input())
    print("Please enter Bop's weight:")
    bop = float(input())

    # Ask user what he wants to do
    print("\nWhat would you like me to calculate?The sum of their weights of the avarage weight?")
    a = input()
    if (a == "sum"):
      print("\nThe sum of Beep's and Bop's weights is ", sum_weights(beep, bop))
    elif (a == "avarage"):
      print("\nThe avarage weight of Beep and Bop is ", calc_avg_weight(beep, bop))

  # Call filter
  run()
