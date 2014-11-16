#!/usr/bin/env python

import sys
import numpy as np
from face import Face, get_faces_by_id

debug = False


class EigenFaces(object):

    """EigenFaces."""

    def __init__(self, faces):
        """Construct EigenFaces object."""
        hangman = faces[0].vector

        for face in faces[1:]:
            hangman = np.hstack((hangman, face.vector))

        self.average = np.divide(hangman.sum(axis=1), float(len(faces)))

        # self.matrix = np.subtract(faces[0].vector, self.average)
        # for face in faces[1:]:
        #     current_face = np.subtract(face.vector, self.average)
        #     self.matrix = np.hstack((self.matrix, current_face))

        # # GET EIGENVECTORS
        # matrix_t = np.transpose(self.matrix)
        # not_covariance = np.dot(matrix_t, self.matrix)
        # all_eigenvalues, all_eigenvectors = np.linalg.eig(not_covariance)
        # good_eigenvalues = sorted(
        #     enumerate(all_eigenvalues),
        #     key=lambda x: x[1]
        # )[-1:]
        # good_indices = [col for col, eig in good_eigenvalues]
        # eigenvectors = all_eigenvectors[:, good_indices]

        # # GET EIGENFACES
        # eigenvectors = np.dot(
        #     self.matrix,
        #     eigenvectors
        # )

        # # NORMALIZING
        # for column in range(np.shape(eigenvectors)[1]):
        #     current_column = eigenvectors[:, column]
        #     if debug:
        #         faces[column].vector = current_column
        #         faces[column].img.show()
        #     norm = np.linalg.norm(current_column)
        #     eigenvectors[:, column] = np.divide(
        #         current_column, norm
        #     )

        # self.eigenvectors_t = np.transpose(eigenvectors)

        # self.average_weight = self.average_weightvector()

    def weightvector(self, face):
        """Return weight vector."""
        weight = np.dot(
            self.eigenvectors_t,
            np.subtract(face, self.average)
        )
        return weight

    def distance(self, vector):
        """Return Eucledian distance to average weight vector."""
        return np.linalg.norm(np.subtract(vector, self.average_weight))

    def similarity(self, face):
        """Return similarity to a face."""
        similarity = self.distance(self.weightvector(face.vector))
        if debug:
            face.vector -= self.average
            face.img.show()
        return similarity

    def similarity_the_dumb_way(self, face):
        """Return similarity to a face the dumb way."""
        lolface = Face('database/1_2_.gif')
        lolface.vector = face.vector - self.average
        if debug:
            lolface.img.show()
        return np.linalg.norm(lolface.vector)

    def average_weightvector(self):
        """Return average weight vector."""
        vector = self.weightvector(self.matrix[:, 0])
        for column in range(1, np.shape(self.matrix)[1]):
            current_weight = self.weightvector(self.matrix[:, column])
            vector = np.hstack((vector, current_weight))

        vector = np.divide(
            vector.sum(axis=1), float(np.shape(self.eigenvectors_t)[1])
        )

        return vector


def get_id_the_dumb_way(face):
    """Return ID the dumb way."""
    similarities = []
    for i in range(1, 16):
        eigenfaces = EigenFaces(get_faces_by_id(i))
        similarities.append(
            (i, eigenfaces.similarity_the_dumb_way(face))
        )

    return sorted(similarities, key=lambda x: x[1])[0]


def test_id_the_dumb_way(id_name):
    """Test ID the dumb way."""
    faces = get_faces_by_id(id_name)
    eigenfaces = EigenFaces(faces)

    similarities = []
    for i in range(1, 16):
        faces = get_faces_by_id(i)
        for face in faces:
            similarities.append(
                (i, face.sub_id,
                 eigenfaces.similarity_the_dumb_way(face))
            )

    print similarities
    return sorted(similarities, key=lambda x: x[2])[0]


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) == 2 else 'database/2_5_.gif'
    face = Face(path)
    print get_id_the_dumb_way(face)
