import pygame
from constants import *
from Cell import Cell
from sudoku_generator import *
class Board:
    def __init__(self, width, height, screen, difficulty ):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.value = generate_sudoku(9, difficulty)
        self.bored = [[None for i in range(9)] for j in range(9)]
        for i in range(0,9):
            for j in range(0,9):
                self.bored[i][j] = Cell(self.value[i][j], i, j, screen)
        self.selected_row = None
        self.selected_col = None



    def draw(self):
        #Draws the board's lines
        for i in range(0, 9):
            for j in range(0, 9):
                self.bored[i][j].draw()
        pygame.draw.line(self.screen, BLACK, (300, 0), (300, 900), width=8)
        pygame.draw.line(self.screen, BLACK, (600, 0), (600, 900), width=8)
        pygame.draw.line(self.screen, BLACK, (0, 300), (900, 300), width=8)
        pygame.draw.line(self.screen, BLACK, (0, 600), (900, 600), width=8)

    def select(self,row ,col):
        if self.selected_row != None and self.selected_col != None:
            self.bored[self.selected_row][self.selected_col].selected = False
        self.bored[row][col].selected = True
        self.selected_row = row
        self.selected_col = col

    def click(self, x, y ):
        # Checks if user inputs is within bounds of the board
        if x < 900 and y < 900:
            col = x//100
            row = y//100
            return (row, col)
        return None
    def place_skectchedvalue(self):
        if self.bored[self.selected_row][self.selected_col].sketched_value > 0:
            self.bored[self.selected_row][self.selected_col].set_cell_value(self.bored[self.selected_row][self.selected_col].sketched_value)
    def clear(self):
        # Clears the board of all user inputs
        if self.bored[self.selected_row][self.selected_col].user_edit == True:
            self.bored[self.selected_row][self.selected_col].set_cell_value(0)
            self.bored[self.selected_row][self.selected_col].set_sketched_value(0)

    def sketch(self, value):
        # Sketches users inputs
        self.bored[self.selected_row][self.selected_col].set_sketched_value(value)

    def place_number(self, value):
        # Places users inputs
        self.bored[self.selected_row][self.selected_col].set_cell_value(value)

    def reset_to_original(self):
        # Changes only the user modified cells back to 0
        for i in range(0, 9):
            for j in range(0, 9):
                if self.bored[i][j].user_edit == True:
                    self.bored[i][j].set_cell_value(0)
                    self.bored[i][j].set_sketched_value(0)


    def is_full(self):
        # Checks to see if any cell is empty if none are empty return that it is full
        for i in range(0, 9):
            for j in range(0, 9):
                if self.bored[i][j].value == 0:
                    return False
        return True

    def update_board(self):
        # Loops through board creating a new board with the new values
        updated_board = []
        for i in range(0, 9):
            updated_values = []
            for j in range(0, 9):
                updated_values.append(self.bored[i][j].value)
            updated_board.append(updated_values)
        return updated_board

    def find_empty(self):
        # Loops through board to see if any value is = 0
        for i in range(0, 9):
            for j in range(0, 9):
                if self.bored[i][j].value == 0:
                    return i, j
        return None

    def check_board(self):
        if not self.is_full():
            return False
        board_values = self.update_board()
        for index in range(0, 9):
            # Selects the entirety of a specific row or column
            row = board_values[index][:]
            col = board_values[:][index]
            if len(row) != len(set(row)) or len(col) != len(set(col)):
                return False
        for x_position in range(0, 1, 3):
            for x_position in range(0, 7, 3):
                small_box = []
                # Starts top left of smaller box counts two to the right
                for i in range(x_position, x_position + 2):
                    # Starts top left of smaller box counts two down
                    for j in range(x_position, x_position + 2):
                        val = board_values[i][j]
                        # Checks to see if value already exists
                        if val in small_box:
                            return False
                        small_box.append(val)
        return True








