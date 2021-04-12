boardSize = 20
import numpy as np
import pygame
import time

true = True
false = False
Live = (50, 50, 50)
Dead = (255, 255, 255)


def initialGameState(gameBoard):
    gameBoard[0][2] = 1
    gameBoard[1][3] = 1
    gameBoard[2][1] = 1
    gameBoard[2][2] = 1
    gameBoard[2][3] = 1
    return gameBoard


# returns a 2d array with the cells directly surrounding the home coordinates
# fills in padding to ensure a square return
# this currently only works with d=1 due to padding. Generalization can be implemented later
def surroundingState(n, x, d=1):
    value = x[max(0, n[0] - d):min(boardSize, n[0] + d + 1), max(0, n[1] - d):min(boardSize, n[1] + d + 1)]
    # if on far left edge
    if n[1] == 0:
        value = np.append(np.zeros((value.shape[0], 1)), value, axis=1)
    if n[0] == 0:
        value = np.append(np.zeros((1, 3)), value, axis=0)
        ## TODO These next two need to be checked. There is something wrong with them
    if n[0] == boardSize:
        value = np.append(value, np.zeroes((2, 1), axis=1))
    if n[1] == boardSize:
        value = np.append(value, np.zeros((3, 1)), axis=0)

    return value

def updateScreen(Gameboard):
    x = 0
    # cell = Rect()

    while x < boardSize:
        y = 0
        while y < boardSize:
            cellColour = Gameboard[x][y]
            if cellColour > 0:
                cellColour = Dead
            else:
                cellColour = Live
            pygame.draw.rect(screen, cellColour, (20 + x * 22, 20 + y * 22, 20, 20), border_radius=1)
            y += 1
        x += 1
    pygame.display.update()

    nextboard = np.zeros((boardSize, boardSize))

    for i in range(len(Gameboard) - 1):
        for j in range(len(Gameboard) - 1):
            neighbours = np.sum(surroundingState((i, j), Gameboard))

            # Birth rule
            if neighbours == 3 and Gameboard[i, j] == 0:
                nextboard[i, j] = 1

            # Death by isolation
            elif neighbours <= 2 and Gameboard[i, j] == 1:
                nextboard[i, j] = 0

            # Death by overcrowding
            elif neighbours >= 5 and Gameboard[i, j] == 1:
                nextboard[i, j] = 0

            # Survival
            elif (neighbours == 3 or neighbours == 4) and Gameboard[i, j] == 1:
                nextboard[i, j] = 1

    Gameboard = nextboard
    return Gameboard
    #  print(Gameboard)




if __name__ == '__main__':
    # todo add click to add cell functionality
    Gameboard = np.zeros((boardSize, boardSize))
    Gameboard = initialGameState(Gameboard)
    print(Gameboard)
    pygame.init()
    screen = pygame.display.set_mode((640, 240 * 2))
    screen.fill((0, 0, 0))
    # todo add pause button
    pygame.draw.rect(screen, (255, 255, 0), [500, 20, 100, 40])
    font = pygame.font.SysFont(None, 24)
    BLUE = (0,0,255)
    img = font.render('Pause', True, BLUE)
    screen.blit(img, (510, 20))


    x = 0
    # cell = Rect()
    updateScreen(Gameboard)
    lastFrameUpdate = time.time()
    running = true
    while running:
        start = time.time()
        if time.time() - lastFrameUpdate >= 0.4:
            Gameboard = updateScreen(Gameboard)
            lastFrameUpdate = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = false

        print()

