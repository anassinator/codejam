#!/usr/bin/env python
import numpy as np

class Faces(object):
    def __init__(self,matrix):
        self.matrix = matrix
        self.matrix = self.matrix.reshape(self.height * self.width,1)

class EigenFaces(object):
    def __init__(self,faces):
        self.matrix = []
        for face in faces:
            self.matrix.append(face)
    
    def calculatingEigenVector(self):
        covariance = np.dot(np.transpose(self.matrix), self.matrix)
        eigenVector = np.linalg.eig(covariance)
        return eigenVector
    
    def calculatingAverage(self):
        result = []
        for x in range(0,len(self.matrix)):
            print self.matrix[x]
            a = 0
            for y in range(0,len(self.matrix[x])):
                a =  a +  self.matrix[y][x]
            a = a / (len(self.matrix[x]) + 1)
            print a
            result.append(a)
        return result

def main():
    face1 = np.arange(20)
    face2 = np.arange(20)
    a = [face1,face2]
    eigenface = EigenFaces(a)
    print a
    print eigenface.calculatingAverage()


if __name__ == '__main__':
    main()
