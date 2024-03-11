import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Make random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot graph
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10,6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=1)
    ax.set_aspect('equal') # Both x and y have equal spacing

    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    # Conditional for continue
    keep_runing = 'quit'
    if keep_runing == 'quit':
        break