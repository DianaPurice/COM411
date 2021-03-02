# print(type(variable))
print("what is your name?)
name = input()
print("What is your age?")
age = int(input())
print("What is your bank balange?")
bank = float(input())
print("Welcome {}. You are said to be {} years old. Your bank balance is{}.".format(name, age, bank))


if len(name) > 9:
  print("You have a really long name!")
print("This is the END of the program!")