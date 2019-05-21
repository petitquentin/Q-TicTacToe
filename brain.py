# -*- coding: utf-8 -*-

import numpy as np

class Brain():
    def __init__(self):
        self.matrix=[]

    # This function allows you to create an initial file that will serve as a "brain". It takes as a "path" argument that defines the path of the file. 
    # Because it is a Numpy object, we could have used the save function, but this will allow us to have a readable file. 
    def reset(self, path):
        self.matrix=[]
        i = 111111111
        while(i < 333333334): 
        # We will look for each number to see if it is a possible combination of grid
        # I know that this solution is not optimal and that many will be tested for nothing, but I have not found how to do better.
            j = 0
            result = 0
            string_i = str(i)
            for j in range (9): # We test if the number is composed of only 1 and 2 and 3
                if(string_i[j] == "1" or string_i[j] == "2" or string_i[j] == "3" ):
                    result = result + 1
            if(result == 9): # If yes, we create a new line. Else, we stop and go to the next number
                line = [i]
                for j in range(9):
                    if(string_i[j] == '3'):
                        line.append(50) # 3 represents an empty cell, so we initialize a score of 50 since it is possible to play in this cell
                    else:
                        line.append(0)
                self.matrix.append(line) # Add the line to the matrix
            i = i + 1
        # We need to save the matrix to the file
        file = open(path, "w")
        for i in range (len(self.matrix)):
            for j in range (9):
                file.write(str(self.matrix[i][j]))
                file.write(" ")
            file.write(str(self.matrix[i][9]))
            file.write("\n")
        file.close()

    # Function that allows to load an existing "brain" matrix. It takes as a "path" argument that defines the path of the file. 
    def load_brain(self, path):
        self.matrix = []
        file = open(path, "r")
        lines = file.readlines()
        

        for line in lines:
            data = line.split()
            data = list(map(float, data))
            self.matrix.append(data)
        file.close()

