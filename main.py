


boardSize = 20
import numpy as np
from future.moves import tkinter as tk
import pygame as pg




def initialGameState(Gameboard ):
    Gameboard[0][2] = 1
    Gameboard[1][3] = 1
    Gameboard[2][1] = 1
    Gameboard[2][2] = 1
    Gameboard[2][3] = 1
    return Gameboard


# returns a 2d array with the cells directly surrounding the home coordinates
# fills in padding to ensure a square return
# this currently only works with d=1 due to padding. Generalization can be implemented later
def surroundingState(n, x, d=1):
    value = x[max(0, n[0] - d):min(boardSize, n[0] + d + 1), max(0, n[1] - d):min(boardSize, n[1] + d + 1)]
    #if on far left edge
    if n[1] == 0 :
        value = np.append(np.zeros((value.shape[0],1)),value,axis = 1)
    if n[0] == 0:
        value = np.append(np.zeros((1,3)),value,axis = 0)
        ## TODO These next two need to be checked. There is something wrong with them
    if n[0] == boardSize:
        value = np.append(value,np.zeroes((2,1),axis=1))
    if n[1]== boardSize:
        value = np.append(value,np.zeros((3,1)),axis = 0)


    return value


if __name__ == '__main__':
    #TODO implement visual board
    Gameboard = np.zeros((boardSize, boardSize))
    Gameboard = initialGameState(Gameboard)
    print(Gameboard)
    simulations = 1000
    count = 0
    while count < simulations:
        nextboard = np.zeros((boardSize, boardSize))

        for i in range(len(Gameboard) - 1):
            for j in range(len(Gameboard) - 1):
                neighbours = np.sum(surroundingState((i, j),Gameboard))

                # Birth rule
                if neighbours == 3 and Gameboard[i, j] == 0:
                    nextboard[i, j] = 1

                # Death by isolation
                elif neighbours <= 2 and Gameboard[i, j] == 1:
                    nextboard[i, j] = 0

                # Death by overcrowding
                elif neighbours >= 5 and Gameboard[i,j] == 1:
                    nextboard[i, j] = 0

                # Survival
                elif (neighbours == 3 or neighbours == 4) and Gameboard[i, j] == 1:
                    nextboard[i, j] = 1

        Gameboard = nextboard
        print(Gameboard)
        print()
        count = count + 1
