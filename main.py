# -*- coding: utf-8 -*-

import datetime
from variables import *
from brain import *
import os

if __name__ == '__main__':

    print(datetime.datetime.now())
    brain = Brain()
    try: #We check if the brain 1 file exists
        check = open('brain/'+NAMEBRAIN+'.txt', 'r')
        check.close()
        # If the file exists
        brain.load_brain('brain/'+NAMEBRAIN+'.txt')
    except FileNotFoundError:
        print("Brain 1 has not been found, we will initailize it")
        brain.reset('brain/'+NAMEBRAIN+'.txt')
    ## Technically, the matrix is now initialized or loaded




