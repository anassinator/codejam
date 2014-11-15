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
