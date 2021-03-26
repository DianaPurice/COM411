# Create function search
def search(file_path):
  # Display message
  print("Seraching...")
  # Create loop
  with open(file_path) as file:
    for line in file.readlines():
      print(f"Looked in {line.strip()}")
  print("...Done!")

# Create function run
def run():
  search("data/files/txt/locations.txt")

# Call function run
run()