"""Face."""

from PIL import Image, ImageFilter
import numpy as np
import time
import os


class Face(object):

    """Face from database."""

    def __init__(self, path):
        """Construct Face."""
        self.path = path
        original = Image.open(path)
        original = original.resize((int(s / 4) for s in original.size))
        self.img = self.face(original)

        filename = os.path.basename(path)
        self.id = int(filename.split('_')[0])
        self.sub_id = int(filename.split('_')[1])

    def __str__(self):
        """Return string representation of Face."""
        return "{img.id:3} {img.sub_id}".format(img=self)

    @staticmethod
    def edges(img):
        """Find edges of image."""
        smooth = img.filter(ImageFilter.BLUR)
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

    def face(self, img):
        """Return face."""
        edges = Face.edges(img)
        leftside_face = self._get_left_median(edges)
        rightside_face = self._get_right_median(edges)

        face_center = (leftside_face + rightside_face) / 2
        left_edge_crop = face_center - img.size[1] / 2
        right_edge_crop = face_center + img.size[1] / 2

        return img.crop(
            [left_edge_crop, 0, right_edge_crop, img.size[1]]
        )

    def _get_left_median(self, img):
        """Return the mean of the left side of the image."""
        width = img.size[0]
        height = img.size[1]

        left_most_points = []
        for y in range(int(height / 5), int(6 * height / 7)):
            row = [
                (img.getpixel((x, y)), x)
                for x in range(10, width / 2)
            ]
            sorted_row = sorted(row)

            left_most_points.append(sorted_row[-1][1])

        return int(np.median(left_most_points))

    def _get_right_median(self, img):
        """Return the mean of the right side of the image."""
        width = img.size[0]
        height = img.size[1]

        right_most_points = []
        for y in range(int(height / 5), int(6 * height / 7)):
            row = [
                (img.getpixel((x, y)), x)
                for x in range(width - 10, width / 2, -1)
            ]
            sorted_row = sorted(row)

            right_most_points.append(sorted_row[-1][1])

        return int(np.median(right_most_points))


def get_faces_by_id(id_name=None):
    """Get images."""
    faces = []
    id_name = "{id}_".format(id=id_name) if id_name else ''
    for root, directories, filenames in os.walk('database'):
        for filename in filenames:
            if filename.startswith(id_name) and '_' in filename:
                path = os.path.join(root, filename)
                faces.append(Face(path))

    return faces


if __name__ == '__main__':
    for face in get_faces_by_id(1):
        face.img.show()
        time.sleep(0.5)
