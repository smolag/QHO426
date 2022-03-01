health = int(input("Please input the number of lives: "))
energy = int(input("Please input the energy level: "))
shield = int(input("Please enter the shield level: "))

print("Health has been set.")

h = "\u2665"
e = "\u2666"
s = "\u2666"

print(f"Lives: {health * h}")
print(f"Energy: {energy * e}")
print(f"Shield: {shield * s}")