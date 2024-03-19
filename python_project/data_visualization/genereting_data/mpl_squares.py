import matplotlib.pyplot as plt


input_values = [number for number in range(1,11)]
squares = [number ** 2 for number in range(1,11)]


# Fig = figuere ; ax = single plot
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set achar title and label axes
ax.set_title("Squares numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)


plt.show()