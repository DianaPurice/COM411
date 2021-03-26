def run():
  # Ask user for beeps levels
  print("What is the lives level?")
  lives = int(input())
  print("\nWhat is the level of energy?")
  energy = int(input())
  print("\nWhat is the level of shield?")
  shield = int(input())
  # Displaying processing message
  print("\nAdjusting the levels...")

  # Displaying results

  print("\nLives: " + "x" * lives)
  print("Energy: " + "x" * energy)
  print("Shield: " + "x" * shield)
