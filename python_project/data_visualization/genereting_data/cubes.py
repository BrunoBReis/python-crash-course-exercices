import matplotlib.pyplot as plt

x_values = range(1,5_001)
y_values = [value ** 3 for value in x_values]


# Set graph
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set char title and label axes
ax.set_title("Cubic numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubic of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# Set range for each exis
ax.axis([0, max(x_values) * 1.1, 0, max(y_values) * 1.1])
# ax.ticklabel_format(style='sci')

plt.show()
