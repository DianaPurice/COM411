print("How many times to print the symbol?")
x = int(input())

# i is a counter. it keeps track of how many times we went through the loop
i = 0


while i < x: # condition for reapeating the code - as long as i lower than x
  print("\u27BD \n", i)
  i += 1 # new value of the counter is one more than the counter
print("We left the loop")

# u can set i to 1 and change i < x to i <= x !not good for computer