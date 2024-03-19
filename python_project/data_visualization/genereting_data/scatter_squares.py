import matplotlib.pyplot as plt
from pathlib import Path

file_path = Path('python_project/data_visualization/figures/squares.png')

x_values = range(1,1001)
y_values = [number ** 2 for number in x_values]


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, color=(0, 0.8, 0) ,s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues ,s=10)

# Set char title and label axes
ax.set_title("Squares numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

# Set range for each exis
ax.axis([0, max(x_values) * 1.1, 0, max(y_values) * 1.1])
ax.ticklabel_format(style='plain')

# plt.show()
plt.savefig(file_path, bbox_inches='tight')