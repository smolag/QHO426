print("Program started")
x = abs(int(input("Please enter an ASCII character: ")))

# if x >= 32 and x <= 126:

if x in range(32, 127):

  code = chr(x)
  character = x
  
  print(f"The character represented by the ASCII code {code} is {character}.")
  
else:
  print("Oh, noes!")

print("Program ended!")