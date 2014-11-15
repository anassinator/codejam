#!/usr/bin/env python
import numpy as np

class EigenFaces(object):
    def __init__(self,faces):
        self.matrix = []
        for face in faces:
            self.matrix.append(face)
    
    def eigenvector(self):
        covariance = np.dot(np.transpose(self.matrix), self.matrix)
        eigenVector = np.linalg.eig(covariance)
        return eigenVector
    
    def average(self):
        result = self.matrix[0]
        for x in range(1,len(self.matrix)):
            result = np.add(result,self.matrix[x])
        return result/float(len(self.matrix))

def main():
    face1 = np.arange(20)
    face2 = np.arange(1,40,2)
    a = [face1,face2]
    eigenface = EigenFaces(a)
    print eigenface.eigenvector()
    print eigenface.average()


if __name__ == '__main__':
    main()
