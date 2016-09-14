"""
This program is for building Minesweeper the game
"""

import random
from tkinter import *

"""
Defines the number of boxes and mines based upon desired
difficulty level
"""
difficulty = input('What difficulty do you want to play?\n')

if difficulty == 'Easy':
    xboxes, yboxes, mines = 10, 10, 30

elif difficulty == 'Medium':
    xboxes, yboxes, mines = 20, 20, 60

elif difficulty == 'Hard':
    xboxes, yboxes, mines = 30, 30, 90


class MinesweeperError(Exception):
    pass


class MinesweeperBoard(object):
    """
    Builds the board for the appropriate
    difficulty level and randomly disperses
    bombs and appropriate number tags
    """

    def __init__(self):
        """
        Initializes the Minesweeper Board and calls on
        the __create_board method to store the board in
        the variable self.board
        """

        self.board = self.__create_board()

    def __create_board(self):
        # initializes the variables for the board and row/column counter
        # variables
        board = []

        # Builds a blank 2D board list based upon the desired difficulty
        for row in range(yboxes):
            board.append([])

            for col in range(xboxes):
                board[row].append([])

        # Randomly populates the map with the specified number of mines

        yboxes_list = list(range(yboxes))
        xboxes_list = list(range(xboxes))

        while mines > 0:

            random.shuffle(yboxes_list)
            for row in yboxes_list:

                random.shuffle(xboxes_list)
                for col in xboxes_list:

                    if random.random() > 0.5:
                        board[row][col] = 'M'
                        mines -= 1

                    else:
                        board[row][col] = 0

        # Populates the number spaces on the board based upon
        # the number of adjacent mine spaces
        for row in range(yboxes - 1):
            for col in range(xboxes - 1):
                if board[row][col] != 'M':

                    if row < (yboxes - 1) and col < (xboxes - 1):
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                if board[row + i][col + j] == 'M':
                                    board[row][col] += 1

                    elif row == (yboxes - 1) and col < (xboxes - 1):
                        for i in range(-1, 1):
                            for j in range(-1, 2):
                                if board[row + i][col + j] == 'M':
                                    board[row][col] += 1

                    elif row < (yboxes - 1) and col == (xboxes - 1):
                        for i in range(-1, 2):
                            for j in range(-1, 1):
                                if board[row + i][col + j] == 'M':
                                    board[row][col] += 1

                    elif row == (yboxes - 1) and col == (xboxes - 1):
                        for i in range(-1, 1):
                            for j in range(-1, 1):
                                if board[row + i][col + j] == 'M':
                                    board[row][col] += 1

        return board


class MinesweeperGame(MinesweeperBoard):
    def __init__(self, difficulty):
        MinesweeperBoard.__init__(self)

        self.win = False
        self.lose = False

    """
    Fix the check_win and check_lose functions
    to work with new board setup
    """

    def check_win(self):
        for row in range(yboxes):
            for col in range(xboxes):
                if self.board[row][col][0] == 'M' and self.board[row][col][1] == 'U':
                    return False

        self.win = True
        return True

    def check_lose(self):
        for row in range(yboxes):
            for col in range(xboxes):
                if self.board[row][col][0] == 'M' and self.board[row][col][1] == 'C':
                    self.lose = True
                    return True

        return False


class MinesweeperUI(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title('Minesweeper')

        self.menu_bar = Menu()
        self.file_menu = Menu(self.menu_bar)

        self.tile_img = PhotoImage(file='tile.gif')
        self.tile = Button(image=self.tile_img, command=self.hello)

        self.game_board = []
        for col in range(xboxes):
            self.game_board.append([])
            for row in range(yboxes):
                self.game_board[col].append(self.tile)

        self.__initUI()

    def __initUI(self):
        self.title('Minesweeper')

        self.file_menu.add_command(label='New Game...', command=self.hello)
        self.file_menu.add_command(label='Quit', command=self.quit)
        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.config(menu=self.menu_bar)

        self.__draw_board()

    def __draw_board(self):
        for col in range(xboxes):
            for row in range(yboxes):
                self.game_board[row][col].pack()

    @staticmethod
    def hello():
        print('Hello World!')

if __name__ == "__main__"
