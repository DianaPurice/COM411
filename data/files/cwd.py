# Import os module
import os

# Create cwd function   
def cwd():
  path = os.getcwd()
  # Display messages
  print(f"The current directory is {path}.")
  print("The directory constins the following:")
  # Create loop
  for file in os.listdir(path):
    print(file)

# Create function run
def run():
  # Display messages
  print("Processing...")
  # Call the function cwd
  cwd()

# Call the function run
run()