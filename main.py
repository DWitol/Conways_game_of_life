# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
boardSize = 20
import numpy as np
Gameboard = np.empty((boardSize, boardSize))
Gameboard[:] = 0
def initialGameState():
    Gameboard[1][1] = 1
    Gameboard[1][2] = 1
    Gameboard[1][3 ] = 1
 ##returns a 2d array with the cells directly surrounding the home coordinates
def surroundingState(n,x = Gameboard,d=1):
    return x[n[0]-d:n[0]+d+1,n[1]-d:n[1]+d+1]





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialGameState()
    print(Gameboard)
    simulations = 10
    count = 0
    finalNeighbour = Gameboard[0:0+3, 0:0+3]
    while(count <= simulations):
        nextboard = np.zeros((boardSize, boardSize))
        for i in range(len(Gameboard)-1):
            for j in range(len(Gameboard)-1):
                #Birth rule
                neighbours = Gameboard[i:i+3, j:j+3]
                neighbours = np.sum(Gameboard[i:i+3, j:j+3] == 1)
                if np.sum(Gameboard[i:i+3, j:j+3] == 1) == 3 and Gameboard[i+1,j+1] == 0: nextboard[i+1,j+1] = 1
                #Death by isolation
                if np.sum(Gameboard[i:i+3, j:j+3] == 1) <= 1 and Gameboard[i+1,j+1] == 1: nextboard[i+1,j+1] = 0
                #Death by overcrowding
                if np.sum(Gameboard[i:i+3, j:j+3] == 1) <= 4 and Gameboard[i+1,j+1] == 1: nextboard[i+1,j+1] = 0
                #survival
                if (np.sum(Gameboard[i:i + 3, j:j + 3] == 1) == 2 or np.sum(Gameboard[i:i + 3, j:j + 3] == 1) == 3) and Gameboard[i+1,j+1] == 1: nextboard[i+1,j+1] = 1

        Gameboard = nextboard
        print(Gameboard)
        print()
        count = count + 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
