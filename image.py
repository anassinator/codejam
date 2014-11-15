"""Image."""

from PIL import Image, ImageFilter
import numpy as np
import os


class DatabaseImage(object):

    """Image from database."""

    def __init__(self, path):
        """Construct DatabaseImage."""
        self.path = path
        self.bmp = Image.open(path)

        filename = os.path.basename(path)
        self.id = int(filename.split('_')[0])
        self.sub_id = int(filename.split('_')[1])

    def __str__(self):
        """Return string representation of DatabaseImage."""
        return "{img.id:3} {img.sub_id}".format(img=self)

    def edges(self):
        """Find edges of image."""
        smooth = self.bmp.filter(ImageFilter.SMOOTH)
        edges = smooth.filter(ImageFilter.FIND_EDGES)
        self.bmp = edges
        # WIP

    @property
    def size(self):
        """Return size of image in (x, y)."""
        return self.bmp.size

    @property
    def matrix(self):
        """Return numpy matrix of image."""
        size = self.size
        matrix = []
        for y in range(size[1]):
            matrix.append([self.bmp.getpixel((x, y)) for x in range(size[0])])

        return np.matrix(matrix)

    def center_face(self):
        leftside_face = self.get_leftside_average()
        rightside_face = self.get_rightside_average()
        face_width = leftside_face - rightside_face
        crop_and_center(face_width)
    
    def crop_and_center(self, face_width):
        whitespace = (200 - face_width)/2
        self.crop((self.get_leftside_average - whitespace), 0, self.get_rightside_average + whitespace, self.size[1])    

    def get_leftside_average(self):
        """Return the value of the Average of the left_most_points."""
        width = self.size[0]
        height = self.size[1]
        left_most_points = []
        for row in range(height):
            for column in range(width):
                if image.getpixel(row, column) > 200:
                    left_most_points.append(row)
                    break

        return np.median(left_most_points)

    def get_rightside_average(self):
        """Return the value of the average of the right_most_points."""
        width = self.size[0]
        height = self.size[1]
        right_most_points = []
        for row in range(height):       
            for column in range(width, -1, -1):     #Indices moving right to left
                if image.getpixel(row column) > 200:
                    right_most_points.append(row)
                    break

        return np.median(right_most_points)

def get_images():
    """Get images."""
    for root, directories, filenames in os.walk('database'):
        for filename in filenames:
            if filename.endswith('.gif'):
                path = os.path.join(root, filename)
                yield DatabaseImage(path)


if __name__ == '__main__':
    for image in get_images():
        image.bmp.show()
        print image.matrix
        break
