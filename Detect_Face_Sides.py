#scan through each row
#when you hit a high intensity pixel store x 
#when you hit a low intensity pixel for more than like 10 pixels set xfinal
#scan each row and store all of the size values in a matrix
#scan through the matrix, when the values remain smooth for a while
#then designate a point for the top right and top left at x init and xfina
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
