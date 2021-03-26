# Create search function  
def search(file_path):
  # Display message
  print("Searching...",end="")
  # Create dictionary empty data
  data = {}
  # Open files
  with open(file_path) as file:
    # Create variable
    section_name = ""
    # Create loop
    for line in file:
      # Create if statement
      if (line.startswith("Section")):
        # Create variable to plit line
        parts = line.split(":")
        section_name = parts[1].strip()
      elif (section_name in data):
        data[section_name].append(line.strip())
      else:
        data[section_name] = [line.strip()]
  print("Done!")
  # Return value
  return data

# Create function run  
def run():
  # Call search function and store it
  data = search("data/files/txt/books.txt")
  
  # Open file
  with open("data/files/txt/generated.csv", "w") as file:
    for section, books in data.items():
      for book in books:
        file.write(f"{section},{book}\n")


run()