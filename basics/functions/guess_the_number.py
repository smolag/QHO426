import random

def guessing():

  minimum = int(input("Please enter a minimum value: "))
  
  maximum = int(input("Please enter a maximum value: "))
  
  x = random.randrange(minimum, maximum)
  
  print(f"I am thinking of a number between {minimum} and {maximum}. Can you guess what it is?")
  
  while True:
    guess = int(input("Enter you guess: "))
  
    if guess < x:
      print("Your guess is too low!")
    elif guess > x:
      print("Your guess is too high!")
    elif guess == x:
      print("The guess is correct!")
      break
    else:
      break
  
    print("Try again!")

guessing()