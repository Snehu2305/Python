import matplotlib.pyplot as plt

ages = [18,19,20,21,22,18,19,21,20,22,23,19]
plt.hist(ages, bins=6, color='skyblue', edgecolor='black')
plt.title("age distribution")
plt.show()