h = input("Are you happy? ").lower()
k = input("Do you know it? ").lower()

if h == "yes" and k == "yes":
  print("Clap your hands!")
elif h == "yes" and k == "no":
  print("Show your hapiness!")
else:
  print("Help is available!")