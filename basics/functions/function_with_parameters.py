def run():
  # Define function climb_ladder
  def climb_ladder(r_s, c_s):
    # Compare the 2 parameters
    if (r_s > c_s):
      print("\nStill some way to go!")
    else:
      print("\nWe are almost there!")

  # Call the function
  climb_ladder(5, 2)
  climb_ladder(2, 5)