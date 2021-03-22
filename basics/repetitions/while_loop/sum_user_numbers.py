print("How many numbers should i be summing?")
nts = int(input())

ns = 0
t = 0

while ns < nts:
  print("please enter number:")
  n = int(input())
  ns +=1
  t = t + n

print(t)