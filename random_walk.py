from random import choice

class RandomWalk:
    """A class for random walk"""
    def __init__(self, num_points = 5000):
        self.num_points = num_points
        # just fixed the number of walks
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determine the direction and distance for a step"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    # changing direction
    def fill_walk(self):
        """A METHOD OF CHANGEIMG DIRECTION AND CHOOSING DISTANCE"""
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
