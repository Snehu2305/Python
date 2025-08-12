n = float(input("Enter your percentage: "))

if n >= 90:
  print("Excellent performance!")
elif n >= 80 and n < 90:
  print("Very good performance")
elif n >= 70 and n < 80:
  print("Good performance")
elif n >= 60 and n < 70:
  print("Average performance")
else:
  print("poor performance")