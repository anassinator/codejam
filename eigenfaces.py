#!/usr/bin/env python
import numpy as np
from image import DatabaseImage as data

class EigenFaces(object):
    def __init__(self,faces):
        self.matrix = []
        for face in faces:
            self.matrix.append(face)

        covariance = np.dot(np.transpose(self.matrix), self.matrix)
    
        self.eigenvalues, self.eigenvectors = np.linalg.eig(covariance)
        self.eigenvectors = self.eigenvectors / np.linalg.norm(self.eigenvectors)
        self.eigenvectors_t = np.transpose(self.eigenvectors)
        
        self.average = self.matrix[0]
        for x in range(1,len(self.matrix)):
            self.average = np.add(self.average,self.matrix[x])
        self.average = np.transpose(self.average/float(len(self.matrix)))
        "print self.average" 
 
    def weightvector(self,face): 
        return np.dot(np.transpose(self.eigenvectors),np.subtract(face,self.average))

    @staticmethod
    def distance(vector1,vector2):
        return np.linalg.norm(vector1-vector2)

    
def main():
    data("/")
    face2 = np.arange(1,40,2)
    face3 = np.arange(1,80,4)
    a = [face1,face2,face3]
    eigenfaces = EigenFaces(a)
    c = eigenfaces.weightvector(face1)
    d = eigenfaces.weightvector(face2)
    print c
    print d

if __name__ == '__main__':
    main()
