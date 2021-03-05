import matplotlib.pyplot as plt
x_values = range(1,125)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values , s=10)
plt.style.use('seaborn')
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Cubes of Numbers", fontsize=25)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Values of cubes", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()