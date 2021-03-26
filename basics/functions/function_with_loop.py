def run():
  # Define function cross_bridge
  def cross_bridge(d):
    for s in range(d):
      # Display each step
      print("Crossed step!")
    
    # Display message
    if (d > 5):
      print("The bridge is collapsing!")
    else:
      print("We must keep going!")

  # Call function
  cross_bridge(3)
  cross_bridge(6)