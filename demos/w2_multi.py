age = int(input("Enter age: "))
children = int(input("Enter number of children: "))

if age > 25 and children > 0:
  print("You are a young parent.")
  print(f"Next year you will be {age + 1} years old!")
elif age > 55 and children > 0:
  print(f"Your children will support you in old age!")
elif age < 18 or children == 1:
  print(f"There's still time to have a child if you want!")
else:
  print("You are not so young. :(")
  print("You are going to live long live!")