# -*- coding: utf-8 -*-

import numpy as np
import random

class Brain():
    def __init__(self):
        self.matrix=[]
        self.victoryCount = 0
        self.defeatCount = 0

    # This function allows you to create an initial file that will serve as a "brain". It takes as a "path" argument that defines the path of the file. 
    # Because it is a Numpy object, we could have used the save function, but this will allow us to have a readable file. 
    def reset(self, path):
        self.matrix=[]
        i = 111111111
        while(i < 333333334): 
        # We will look for each number to see if it is a possible combination of grid
        # I know that this solution is not optimal and that many will be tested for nothing, but I have not found better way to do it.
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
        file = open(path, "w+")
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

    # Function which save the brain, we will use it to save our matrix after training.  It takes as a "path" argument that defines the path of the file. 
    def save_brain(self, path):
        file = open(path, "w")
        for (i in range (len(self.matrix))):
            for j in range (9):
                file.write(str(self.atrix[i][j]))
                file.write(" ")
            file.write(str(self.matrix[i][9]))
            file.write("\n")
        file.close()

    # The variable grid is the square grid containing nine squares arranged in threes. it's a number between 111111111 and 333333333
    def next_move(self, grid):
        
        a = 0 # a et b are the two boundaries of the dichotomy
        b = len(self.matrix)
        while(self.matrix[a][0] != grid or self.matrix[b][0] != grid):
            c = int((a+b)/2) # We take the line approximatly in the middle
            # We'll look where "c" is in relation to "grid" 
            if(self.matrix[c][0] > grid):
                b = c
            else: 
                a = c
        if(self.matrix[a][0] == grid):
            line = a
        else:
            line = b
        # End of the dichotomy
        sum = 0
        for( i in range (1, 10)):
            sum = sum + self.matrice[line][i]
        n = random.uniform(1.000000001, int(sum)+1)
        sum = self.matrix[line][1]
        i = 1
        while(n > sum + 1 and i < 9):
            i = i + 1
            sum = sum +self.matrix[line][i]

        return i, line

    # Function that will update the brain according to the result of the game. 
    # The "result" variable represents the result (0 = defeat, 1 = equality and 2 = victory). 
    # "Move" represents the moves that were played during the game.
    def update_brain(self, result, move = []):
        if(result == 0): # If defeat
            for i in move:
                self.matrix[i[1]][i[0]] = self.matrix[i[1]][i[0]]*(1-DICHOTOMYRATE) + 0.00000001
        elif(result == 1): # If equality
            for i in move:
                self.matrix[i[1]][i[0]] = self.matrix[i[1]][i[0]]*(1-DICHOTOMYRATE) + 30*DICHOTOMYRATE
        else:
            for i in move:
                self.matrix[i[1]][i[0]] = self.matrix[i[1]][i[0]]*(1-DICHOTOMYRATE) + 100*DICHOTOMYRATE
    




