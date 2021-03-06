# Create function search
def search(file_path):
  # Display message
  print("Searching...",end="")
  # Create empty lists
  sections = []
  books = []
  # Open files
  with open(file_path) as file:
    # Create loop
    for line in file:
      # Create if statement to add items to the lists
      if line.startswith("Section"):
        # Create variable to split the text file
        section_name = line.split(":")[1]
        # Append elements
        sections.append(section_name.strip())
      else:
        books.append(line.strip())
  # Display message
  print("Done!")
  # Return result as tuple
  return (sections, books)

# Create function save
def save(file_path, data):
  # Display message
  print("Saving...",end="")
  # Open files
  with open(file_path, "w") as file:
    # Open files
    file.write(f"Sections: {data[0]}\n")
    #file.write(f"Sections: {data[0]}\n")
    file.write(f"Books: {data[1]}\n")
    # Display message
  print("Done!")

# Create function run
def run():
  data = search("data/files/txt/books.txt")
  save("data/files/txt/section-books.txt", data)
  #save("data/files/txt/section-books.txt", data)

run()