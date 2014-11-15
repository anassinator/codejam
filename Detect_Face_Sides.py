import numpy as np

def get_leftside_average(self):
    """Return Array of Left Most Points."""
    width = self.size[0]
    height = self.size[1]
    left_most_points = []
    for row in range(height):
        for column in range(width):
            if image.getpixel(row, column) > 200:
                left_most_points.append(column)
                break

    return np.median(left_most_points)
