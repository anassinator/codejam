#!/usr/bin/env python
import numpy as np
from face import Face, get_faces_by_id


class EigenFaces(object):

    """EigenFaces."""

    def __init__(self, faces):
        """Construct EigenFaces object."""
        hangman = faces[0].vector

        for face in faces[1:]:
            hangman = np.hstack((hangman, face.vector))

        self.average = np.divide(hangman.sum(axis=1), float(len(faces)))

        self.matrix = np.subtract(faces[0].vector, self.average)
        for face in faces[1:]:
            current_face = np.subtract(face.vector, self.average)
            self.matrix = np.hstack((self.matrix, current_face))

        # GET EIGENVECTORS
        matrix_t = np.transpose(self.matrix)
        not_covariance = np.dot(matrix_t, self.matrix)
        all_eigenvalues, all_eigenvectors = np.linalg.eig(not_covariance)
        good_eigenvalues = sorted(
            enumerate(all_eigenvalues),
            key=lambda x: x[1]
        )[-3:]
        good_indices = [col for col, eig in good_eigenvalues]
        eigenvectors = all_eigenvectors[:, good_indices]

        # GET EIGENFACES
        eigenvectors = np.dot(
            self.matrix,
            eigenvectors
        )

        # NORMALIZING
        for column in range(np.shape(eigenvectors)[1]):
            current_column = eigenvectors[:, column]
            faces[column].vector = current_column
            norm = np.linalg.norm(current_column)
            eigenvectors[:, column] = np.divide(
                current_column, norm
            )
            faces[column].img.show()

        self.eigenvectors_t = np.transpose(eigenvectors)

        self.average_weight = self.average_weightvector()

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

    def average_weightvector(self):
        """Return average weight vector."""
        vector = self.weightvector(self.matrix[:, 0])
        for column in range(1, np.shape(self.matrix)[1]):
            current_weight = self.weightvector(self.matrix[:, column])
            vector = np.hstack((vector, current_weight))

        vector = np.divide(
            vector.sum(axis=1), float(np.shape(self.eigenvectors_t)[1])
        )
        avg = Face('database/1_2_.gif')
        avg.vector = self.average
        avg.img.show()
        return vector


def main():
    """Main."""
    faces = get_faces_by_id(1)
    eigenfaces = EigenFaces(faces)
    testFace1 = Face('database/1_2_.gif').vector
    testFace2 = Face('database/8_1_.gif').vector

    print eigenfaces.distance(eigenfaces.weightvector(testFace1))
    print eigenfaces.distance(eigenfaces.weightvector(testFace2))

if __name__ == '__main__':
    main()
