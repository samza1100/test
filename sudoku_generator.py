import math, random

class SudokuGenerator:
    # initialize
    def __init__(self, row_length, removed_cells):
        # the length of each row
        self.row_length = row_length
        # the total number of cells to be removed
        self.removed_cells = removed_cells
        # a 2D list of ints to represent the board
        self.board = [[0 for i in range(9)] for j in range(9)]
        # the square root of row_length
        self.box_length = int(math.sqrt(row_length))

    # returns a 2D python list of numbers
    def get_board(self):
        return self.board

    # the board is displayed on the console.
    def print_board(self):
        for i in self.board:
            print(i, end="\n")

    # determines whether num is present in the given row of the board.
    def valid_in_row(self, row, num):
        for i in range(self.row_length):
            if self.board[row][i] == num:
                return False
        return True
    # determines whether num is present in the given column of the board.
    def valid_in_col(self, col, num):
        for i in range(self.row_length):
            if self.board[i][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        """
                box-coordinates
                (0,0),(0,3)(0,6)
                (3,0),(3,3)(3,6)
                (6,0),(6,3)(6,6)
                """
        i, j = 0, 0

        for i in range(3):
            for j in range(3):
                if self.board[row_start + j][col_start + i] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        # x will be what we use to indicate a spot that is availible for the user to insert a value
        # 0 will represent an empty space on the board where a value needs to be inserted for the answer
        if self.valid_in_row( row, num) and self.valid_in_col(col, num) and self.valid_in_box(row-(row % 3), col-(col % 3), num):
            return True
        else:
            return False

    # fills in the 3x3 box at random
    def fill_box(self, row_start, col_start):
        # ensures that no value appears in the box more than once
        random_sample = random.sample(range(1, 10), 9)
        for i in range(row_start, row_start+3):
            for j in range(col_start, col_start+3):
                self.board[i][j] = random_sample[0]
                random_sample.pop(0)

    # fills the three boxes along the board's main diagonal
    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    # completely fills board
    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True
        # uses backtracking
        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    # it creates a solution by using the functions fill_diagonal and fill_remaining
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
    #replaces random cells with 0, given by self.removed_cells (30, 40, or 50)
    def remove_cells(self):
        cells_to_remove = self.removed_cells
        while cells_to_remove != 0:
            rand_1 = random.randint(0, 8)
            rand_2 = random.randint(0, 8)
            if self.board[rand_1][
                rand_2] != 0:
                self.board[rand_1][rand_2] = 0
                cells_to_remove -= 1
    # generates and returns a sudoku board of varying sizes

def generate_sudoku(size, removed):  # argument
    sudoku = SudokuGenerator(size, removed)  # passing in size and removed paramters
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board