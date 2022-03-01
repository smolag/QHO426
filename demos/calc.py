nums = input("Provide two numbers: ").strip()
nums = [float(item) for item in nums.split()]

n1 = nums[0]
n2 = nums[1]

print(f"{n1} + {n2} = {n1 + n2}")
print(f"{n1} - {n2} = {n1 - n2}")
print(f"{n1} * {n2} = {n1 * n2}")
print(f"{n1} / {n2} = {n1 / n2}")
print(f"{n1} ^ {n2} = {n1 ** n2}")