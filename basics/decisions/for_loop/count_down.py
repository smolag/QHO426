distance = int(input("How far are we from the cave? "))

for i in range(distance, 0, -1):
  print(f"{i} steps remaining")
else:
  print("We have reached the cave!")