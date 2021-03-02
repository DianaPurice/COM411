
# print(type(variable))
print("what is your name?")
name = input()
print("What is your age?")
age = int(input())
print("What is your bank balange?")
bank = float(input())
print("Welcome {}. You are said to be {} years old. Your bank balance is{}.".format(name, age, bank))

# play with bool(input()) for true and false = boolean datatype
if len(name) > 9:
  print("You have a really long name!")
elif len(name) > 6:
  print("Your name is a bit long. Consider a nickname.")
elif len(name) < 3:
  print("Your name is veeery short")
else:
  print("Your name is quite okay")
print("This is the END of the program!")