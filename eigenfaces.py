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
        self.average = self.matrix[0]
        for x in range(1,len(self.matrix)):
            self.average = np.add(self.average,self.matrix[x])
        self.average = self.average/float(len(self.matrix))

 
 
def weightvector(self,face): 
    return np.dot(np.transpose(eigenvectors),np.subtract(face,self.average))


    
def main():
    face1 = np.arange(20)
    face2 = np.arange(1,40,2)
    a = [face1,face2]
    eigenface = EigenFaces(a)
    print eigenface.eigenvectors
    print eigenface.eigenvalues
    print eigenface.average

if __name__ == '__main__':
    main()
