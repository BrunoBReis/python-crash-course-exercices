from random import choice


class RandomWalk:
    """Class to generate random walks"""

    def __init__(self, num_points=5_000):
        """Initialize attributes"""
        self.num_points = num_points

        # All walks starts at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points"""

        # Keep taking steps untill reaches num_points
        while len(self.x_values) < self.num_points:
            
            # Decides where and how far to go in x
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            # Decides where and how far to go in y
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Rejects move to nowhere
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculates new position -1 = last position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
    