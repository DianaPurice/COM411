# Ask user how many mountains should be displayed
print("How many mountains should I display?")
m = int(input())

# Display message
print("\nDisplaying...")

# Use for loop to display result
for mn in range(m):
  print()
  print("""
      __
     /  \\\\_ 
    /^    \\\\
   /  ^    \\\\_
 _/ ^ ^     ^\\\\
/  ^      ^   \\\\ """)