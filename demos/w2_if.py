name = input("Enter your name: ")

if len(name) > 9:
  print("Your name is way too long to remember. Can I use a nickname, plese?")
elif len(name) <= 3:
  print("That's very short and easy to remember!")
else:
  print("Your name is pretty short!")

print(f"Nice to meet you anyway, {name}!")