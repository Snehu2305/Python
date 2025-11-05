import matplotlib.pyplot as plt

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
sales=[1000, 1500, 3020, 980, 990, 2100, 6500]

plt.bar(days, sales, color='blue')
plt.title("Sales per day")
plt.xlabel("days")
plt.ylabel("sale")

plt.show()