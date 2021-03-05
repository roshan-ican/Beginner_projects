#1. plotting a simple graph
#2. modifying the data or adding more readibility
#3. Correcting the graph by giving plot() a input and outpput value
#4. Using the built-in styles

import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]
#One of the 5 built in styles
plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
ax.scatter(2, 4, s = 200)
#Giving the input values and linewidth controls the thinkness
ax.plot(input_values, squares, linewidth = 3)


#Set chart's title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Value of squares", fontsize=14)

#set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()