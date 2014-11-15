#!/usr/bin/env python
import numpy as np

class EigenFaces(object):
    def __init__(self,faces):
        self.matrix = []
        for face in faces:
            self.matrix.append(face)

        covariance = np.dot(np.transpose(self.matrix), self.matrix)
        self.eigenvectors = np.linalg.eig(covariance)
        self.eigenvalues = self.eigenvectors[0]
        self.eigenvectors = self.eigenvectors[1]
        self.matrix_t = np.transpose(self.matrix)
        self.average = self.matrix[0]
        print self.average
        for x in range(1,len(self.matrix)):
            self.average = np.add(self.average,self.matrix[x])
        self.average = np.transpose(self.average/float(len(self.matrix)))
        print self.average
 
 
    def weightvector(self,face): 
        return np.dot(np.transpose(self.eigenvectors),np.subtract(face,self.average))
    
    @staticmethod
    def distance(vector1,vector2):
        return np.linalg.norm(vector1-vector2)

    
def main():
    face1 = np.arange(20)
    face2 = np.arange(1,40,2)
    a = [face1,face2]
    eigenfaces = EigenFaces(a)
    """
    print eigenfaces.eigenvectors
    print eigenfaces.eigenvalues
    print np.dot(a,eigenfaces.eigenvectors)
    print eigenfaces.average
    print np.transpose(eigenfaces.average)
    """
    b = eigenfaces.weightvector(face1)
    print b 
    print EigenFaces.distance(b,face1)
    print EigenFaces.distance(b,face2)

if __name__ == '__main__':
    main()
