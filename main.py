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
    return x[max(0,n[0]-d):min(boardSize,n[0]+d+1),max(0,n[1]-d):min(boardSize,n[1]+d+1)]





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initialGameState()
    print(Gameboard)
    simulations = 1
    count = 0
    finalNeighbour = Gameboard[0:0+3, 0:0+3]
    births = 0
    deathByIsolation = 0
    deathByOvercrowding = 0
    survival = 0
    while(count < simulations):
        nextboard = np.zeros((boardSize, boardSize))
        for i in range(len(Gameboard)-1):
            for j in range(len(Gameboard)-1):
                neighbours = surroundingState((i,j))
                #Birth rule
                if np.sum(neighbours == 1) == 3 and Gameboard[i,j] == 0:
                    births = births +1
                    nextboard[i,j] = 1
                #Death by isolation
                if np.sum(neighbours == 1) <= 1 and Gameboard[i,j] == 1:
                    deathByIsolation = deathByIsolation + 1
                    nextboard[i,j] = 0
                #Death by overcrowding
                if np.sum(neighbours == 1) >= 4 and Gameboard[i,j] == 1:
                    deathByOvercrowding = deathByOvercrowding + 1
                    nextboard[i,j] = 0
                #Survival
                if (np.sum(neighbours == 1) == 2 or np.sum(neighbours == 1) == 3) and Gameboard[i+1,j+1] == 1:
                    survival = survival+1
                    nextboard[i+1,j+1] = 1
        print(births,deathByIsolation,deathByOvercrowding,survival)

        Gameboard = nextboard
        print(Gameboard)
        print()
        count = count + 1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
