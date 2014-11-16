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
            self.matrix,
            self.eigenvectors / np.linalg.norm(self.eigenvectors)
        )

        self.eigenvectors_t = np.transpose(self.eigenvectors)
        self.average = self.matrix.sum(axis=1) / float(len(faces))

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
        print 'distance', np.shape(self.average_weight)
        return np.linalg.norm(np.subtract(vector, self.average_weight))

    def average_weightvector(self):
        """Return average weight vector."""
        vector = self.weightvector(self.matrix[:, 0])
        print np.shape(self.matrix[:, 0])
        for column in range(1, np.shape(self.matrix)[1]):
            current_weight = self.weightvector(self.matrix[:, column])
            print current_weight
            vector = np.hstack((vector, current_weight))

        print 'all weights', np.shape(vector), np.shape(self.eigenvectors)
        print vector

        vector = vector.sum(axis=1) / float(np.shape(self.eigenvectors)[1])

        print 'average', np.shape(vector), vector, float(np.shape(self.eigenvectors)[1])
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
