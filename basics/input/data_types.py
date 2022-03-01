name = input("\nWhat is your name human? ")
age = int(input("How old are you (years)? "))
height = float(input("How tall are you (meters)? "))
weight = float(input("How much do you weight(in kg)? "))

bmi = weight / height ** 2

print(f"\n{name}, you are {age} years old and your BMI is {bmi:.2f}.\n")