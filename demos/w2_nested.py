salary = float(input("Enter salary: "))
years = int(input("Provide number of years: "))

if years > 2:
  if salary < 25_000:
    salary *= 1.1
    print(f"Your new salary will be £{salary:.2f}")
  else:
    salary += 100
    print(f"Small change, you will now earn £{salary:.2f}")
elif years >= 1:
  print("No salary increase for you, sorry!")
else:
  if salary < 15_000:
    print("Oops! Your salary will be now £20.000")
    salary = 20_000
print("Let us work for the good of the company.")