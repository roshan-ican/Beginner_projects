#5. plotting and styling individual points with scatter()
#6. plotting the series of points with scatter
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
# adding custom colors
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#set chart, title and label
ax.set_title("Squares Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Values", fontsize=14)

#set the label
ax.axis([0, 1100, 0, 1100000])
ax.tick_params(axis='both', which = 'major', labelsize=14)

plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')