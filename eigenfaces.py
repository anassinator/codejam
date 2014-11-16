#!/usr/bin/env python
import numpy as np
from face import Face, get_faces_by_id


class EigenFaces(object):

    """EigenFaces."""

    def __init__(self, faces):
        """Construct EigenFaces object."""
        self.matrix = faces[0].vector
        for face in faces[1:]:
            self.matrix = np.hstack((self.matrix, face.vector))

        self.matrix_t = np.transpose(self.matrix)
        covariance = self.matrix_t.dot(self.matrix)
        self.eigenvalues, self.eigenvectors = np.linalg.eig(covariance)

        self.eigenvectors = np.dot(
            self.eigenvectors / np.linalg.norm(self.eigenvectors),
            self.matrix_t
        )

        self.eigenvectors_t = np.transpose(self.eigenvectors)
        self.average = self.matrix.sum(axis=1) / float(len(faces))
        self.average = np.transpose(self.average)

        self.average_weight = self.average_weightvector()
        print np.shape(self.average_weight)

    def weightvector(self, face):
        """Return weight vector."""
        return np.dot(
            self.eigenvectors,
            np.subtract(face, self.average)
        )

    def distance(self, vector):
        """Return Eucledian distance between vectors."""
        return np.linalg.norm(vector - self.average_weight)

    def average_weightvector(self):
        """Return average weight vector."""
        vector = self.weightvector(self.matrix[:, 0])
        for column in range(np.shape(self.matrix)[1]):
            vector = np.hstack(
                (vector,
                 self.weightvector(self.matrix[:, column]))
            )

        vector = vector.sum(axis=1) / float(len(self.eigenvectors))
        vector = np.transpose(vector)
        return vector


def main():
    """Main."""
    faces = get_faces_by_id(1)
    eigenfaces = EigenFaces(faces)
    testFace1 = Face('database/1_2_.gif').vector
    testFace2 = Face('database/7_1_.gif').vector
    print eigenfaces.distance(eigenfaces.weightvector(testFace1))
    print eigenfaces.distance(eigenfaces.weightvector(testFace2))

if __name__ == '__main__':
    main()
