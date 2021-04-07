


boardSize = 20
import numpy as np
from future.moves import tkinter as tk
import pygame as pg

class GameBoard(tk.Frame):
    def __init__(self, parent, rows=boardSize, columns=boardSize, size=32, color1="white", color2="blue"):
        '''size is the size of a square, in pixels'''

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def addpiece(self, name, image, row=0, column=0):
        '''Add a piece to the playing board'''
        self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        '''Place a piece at the given row/column'''
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")




def initialGameState(Gameboard ):
    root = tk.Tk()
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    player1 = tk.PhotoImage(board)
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
