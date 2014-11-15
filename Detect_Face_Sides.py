import numpy as np

def get_leftside_average(self):
    """Return the value of the Average of the left_most_points."""
    width = self.size[0]
    height = self.size[1]
    left_most_points = []
    for row in range(height):
        for column in range(width/2):
            if self.bmp.getpixel(row, column) > 200:
                left_most_points.append(column)
                break

    return np.median(left_most_points)

def get_rightside_average(self):
    """Return the value of the average of the right_most_points."""
    width = self.size[0]
    height = self.size[1]
    right_most_points = []
    for row in range(height):       
        for column in range(width, width / 2, -1):     
            if self.bmp.getpixel(row column) > 200:
                right_most_points.append(column)
                break

    return np.median(right_most_points)

