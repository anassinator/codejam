"""Face."""

from PIL import Image, ImageFilter
import numpy as np
import os


class Face(object):

    """Face from database."""

    def __init__(self, path):
        """Construct Face."""
        self.path = path
        self.original = Image.open(path)
        self.img = self.face()

        filename = os.path.basename(path)
        self.id = int(filename.split('_')[0])
        self.sub_id = int(filename.split('_')[1])

    def __str__(self):
        """Return string representation of Face."""
        return "{img.id:3} {img.sub_id}".format(img=self)

    def edges(self):
        """Find edges of image."""
        smooth = self.original.filter(ImageFilter.BLUR)
        edges = smooth.filter(ImageFilter.FIND_EDGES)
        blur = edges.filter(ImageFilter.BLUR)
        return blur

    @property
    def size(self):
        """Return size of image in (x, y)."""
        return self.img.size

    @property
    def vector(self):
        """Return column vector of image intensities."""
        size = self.size
        matrix = []
        for y in range(size[1]):
            matrix.append([self.img.getpixel((x, y)) for x in range(size[0])])

        matrix = np.matrix(matrix)
        return matrix.reshape((size[0] * self.size[1], 1))

    def face(self):
        img = self.edges()
        leftside_face = self.get_leftside_average(img)
        rightside_face = self.get_rightside_average(img)

        face_center = (leftside_face + rightside_face) / 2
        left_edge_crop = face_center - self.original.size[1] / 2
        right_edge_crop = face_center + self.original.size[1] / 2

        return self.original.crop(
            [left_edge_crop, 0, right_edge_crop, self.original.size[1]]
        )

    def get_leftside_average(self, img):
        """Return the value of the average of the left_most_points."""
        width = img.size[0]
        height = img.size[1]

        left_most_points = []
        for y in range(int(height / 5), int(6 * height / 7)):
            row = [
                (img.getpixel((x, y)), x)
                for x in range(width / 10, width / 2)
            ]
            sorted_row = sorted(row, key=lambda x: x[0])

            left_most_points.append(sorted_row[-1][1])

        return int(np.median(left_most_points))

    def get_rightside_average(self, img):
        """Return the value of the average of the right_most_points."""
        width = img.size[0]
        height = img.size[1]

        right_most_points = []
        for y in range(int(height / 5), int(6 * height / 7)):
            row = [
                (img.getpixel((x, y)), x)
                for x in range(9 * width / 10, width / 2, -1)
            ]
            sorted_row = sorted(row, key=lambda x: x[0])

            right_most_points.append(sorted_row[-1][1])

        return int(np.median(right_most_points))


def get_faces():
    """Get images."""
    for root, directories, filenames in os.walk('database'):
        for filename in filenames:
            if filename.endswith('.gif'):
                path = os.path.join(root, filename)
                yield Face(path)


if __name__ == '__main__':
    for face in get_faces():
        # face.img.show()
        print face.size
        print np.shape(face.vector)
        break
