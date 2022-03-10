def cross_bridge(steps):
  for i in range(steps):
    print("Crossed step")
    if i > 5:
      print("The bridge is collapsing!")
  else:
    print("We must keep going!")

cross_bridge(3)