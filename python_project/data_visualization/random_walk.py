from random import choice


class RandomWalk:
    """Class to generate random walks"""

    def __init__(self, num_points=5_000):
        """Initialize attributes"""
        self.num_points = num_points

        # All walks starts at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Get x and y steps"""
        
        direction_value = choice([1,-1])
        distance_value = choice([n for n in range(5)])

        return direction_value * distance_value
    
    
    def fill_walk(self):
        """Calculate all the points"""

        # Keep taking steps untill reaches num_points
        while len(self.x_values) < self.num_points:
            
            x_step = self.get_step()
            y_step = self.get_step()

            # Rejects move to nowhere
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculates new position -1 = last position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
    