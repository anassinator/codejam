#!/usr/bin/env python
import numpy as np
from face import Face 
import os

class EigenFaces(object):
    def __init__(self,faces):
        self.matrix = faces[0]
        for face in faces[1:]:
            np.hstack((self.matrix, face))
        self.matrix_t = np.transpose(self.matrix)
        covariance = self.matrix_t.dot(self.matrix)
    
        self.eigenvalues, self.eigenvectors = np.linalg.eig(covariance)
        self.eigenvectors = np.dot(self.eigenvectors / np.linalg.norm(self.eigenvectors) , self.matrix)
        print self.eigenvectors    
        self.eigenvectors_t = np.transpose(self.eigenvectors)
        
        self.average = self.matrix[0]
        for x in range(1,len(self.matrix)):
            self.average = np.add(self.average,self.matrix[x])
        self.average = np.transpose(self.average/float(len(self.matrix)))
        "print self.average" 
 
    def weightvector(self,face): 
        return np.dot(self.eigenvectors,np.subtract(face,self.average))

    @staticmethod
    def distance(vector1,vector2):
        return np.linalg.norm(vector1-vector2)

    def average_weightvector(self):
        vector = self.weightvector(self,self.matrix[0])
        for x in range(1,len(self.matrix)):
            vector = np.add(vector,self.weightvector(self, self.matrix[x]))
        vector/float(len(eigenfaces.eigenvectors))
        return vector

def main():
    face1 = Face('/CodeJam/database/1_2_.gif').vector
    face3 = Face('/CodeJam/database/1_4_.gif').vector
    face4 = Face('/CodeJam/database/1_5_.gif').vector
    face5 = Face('/CodeJam/database/1_6_.gif').vector
    face6 = Face('/CodeJam/database/1_7_.gif').vector
    face7 = Face('/CodeJam/database/1_9_.gif').vector
    face8 = Face('/CodeJam/database/1_10_.gif').vector
    face9 = Face('/CodeJam/database/1_11_.gif').vector
    a = [face1, face3, face4, face5, face6, face7, face8, face9]
    eigenfaces = EigenFaces(a)
    testFace1 = Face('/CodeJam/database/1_2_.gif').vector
    testFace2 = Face('/CodeJam/database/7_1_.gif').vector
    print eigenfaces.distance(eigenfaces.weightvector(testFace1),eigenfaces.average_weightvector())
    print eigenfaces.distance(eigenfaces.weightvector(testFace2),eigenfaces.average_weightvector())

if __name__ == '__main__':
    main()
