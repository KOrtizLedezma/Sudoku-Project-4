import math
import random

board1 = [[0 for _ in range(9)] for _ in range(9)]

class SudokuGenerator:
    # create a sudoku board - initialize class variables and set up the 2D board
    # This should initialize:
    # self.row_length		- the length of each row
    # self.removed_cells	- the total number of cells to be removed
    # self.board			- a 2D list of ints to represent the board
    # self.box_length		- the square root of row_length
    # Parameters:
    # row_length is the number of rows/columns of the board (always 9 for this project)
    # removed_cells is an integer value - the number of cells to be removed
    # Return: None

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for num in range(row_length)] for num in range(row_length)]
        self.box_length = int(math.sqrt(row_length))

    # Returns a 2D python list of numbers which represents the board
    # Parameters: None
    # Return: list[list]
    def get_board(self):
        return self.board

    # Displays the board to the console
    # This is not strictly required, but it may be useful for debugging purposes
    # Parameters: None
    # Return: None

    def print_board(self): #Prints the board all joined together. 
        for num in range(len(self.board)):
            print(''.join(str(self.board[num])))

    # Determines if num is contained in the specified row (horizontal) of the board
    # If num is already in the specified row, return False.
    # Otherwise, return True
    # Parameters:
    # row is the index of the row we are checking
    # num is the value we are looking for in the row
    # Return: boolean

    def valid_in_row(self, row, num):
        for slot_num in self.board[row]:
            if num == slot_num:
                return False
        return True

    # Determines if num is contained in the specified column (vertical) of the board
    # If num is already in the specified col, return False.
    # Otherwise, return True
    # Parameters:
    # col is the index of the column we are checking
    # num is the value we are looking for in the column
    # Return: boolean

    def valid_in_col(self, col, num):
        for row in range(len(self.board)):
            col_num = self.board[row][col]
            if num == col_num:
                return False
        return True

    # Determines if num is contained in the 3x3 box specified on the board
    # If num is in the specified box starting at (row_start, col_start), return False.
    # Otherwise, return True
    # Parameters:
    # row_start and col_start are the starting indices of the box to check
    # i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)
    # num is the value we are looking for in the box
    # Return: boolean

    def valid_in_box(self, row_start, col_start, num):
        row_start = row_start - (row_start % 3) # Modulus is used in order to get row_start and col_start to the starting indices of the certain boxes. 
        col_start = col_start - (col_start % 3) # This basically sets any number that isn't 0, 3, or 6 to these numbers within their respective ranges. 
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start + 3):
                if self.board[row][col] == num:
                    return False
        return True

    # Determines if it is valid to enter num at (row, col) in the board
    # This is done by checking that num is unused in the appropriate, row, column, and box
    # Parameters:
    # row and col are the row index and col index of the cell to check in the board
    # num is the value to test if it is safe to enter this cell
    # Return: boolean

    def is_valid(self, row, col, num):
        if self.valid_in_box(row, col, num) and self.valid_in_col(col, num) and self.valid_in_row(row, num):
            return True
        else:
            return False

    # Fills the specified 3x3 box with values
    # For each position, generates a random digit which has not yet been used in the box
    # Parameters:
    # row_start and col_start are the starting indices of the box to check
    # i.e., the box is from (row_start, col_start) to (row_start+2, col_start+2)
    # Return: None

    def fill_box(self, row_start, col_start):
        num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] #This list is used in order to serve as another check so items don't repeat within a box. 
        for row in range(row_start, row_start + 3):
            for cell in range(col_start, col_start + 3):
                random_num = random.choice(num_list)
                self.board[row][cell] = random_num
                num_list.remove(random_num) #Basically removes the number out of the list so it isn't able to be chosen again.

    # Fills the three boxes along the main diagonal of the board.
    # These are the boxes which start at (0,0), (3,3), and (6,6)
    # Parameters: None
    # Return: None

    def fill_diagonal(self):
        for diagonal in range(0, 6 + 1, 3): #The range will basically alwasy step by 3 and stop at 7 so it accounts for the starting point (6,6).
            self.fill_box(diagonal, diagonal)

    # DO NOT CHANGE
    # Provided for students
    # Fills the remaining cells of the board
    # Should be called after the diagonal boxes have been filled
    # Parameters:
    # row, col specifies the coordinates of the first empty (0) cell
    # Return:
    # boolean (whether we could solve the board)

    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
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

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    # DO NOT CHANGE
    # Provided for students
    # Constructs a solution by calling fill_diagonal and fill_remaining
    # Parameters: None
    # Return: None

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    # Removes the appropriate number of cells from the board
    # This is done by setting some values to 0
    # Should be called after the entire solution has been constructed
    # i.e. after fill_values has been called
    # NOTE: Be careful not to 'remove' the same cell multiple times
    # i.e. if a cell is already 0, it cannot be removed again
    # Parameters: None
    # Return: None

    def remove_cells(self):
        successful_attempts = 0 #Takes into account the number of successful attempts to remove a number. 
        for row in range(0, 5000): #The range is so high so it accounts for the times it turns a number into 0 more than once. 
            random_num1 = random.randint(0, 8)
            random_num2 = random.randint(0, 8)
            if successful_attempts < self.removed_cells:
                if self.board[random_num1][random_num2] != 0:
                    self.board[random_num1][random_num2] = 0
                    successful_attempts += 1
                elif self.board[random_num1][random_num2] == 0:
                    pass
            elif successful_attempts == self.removed_cells: #When successful attempts reaches the amount of desired cells that are to be removed, it breaks. 
                break

            # DO NOT CHANGE


# Provided for students
# Given a number of rows and number of cells to remove, this function:
# 1. Creates a SudokuGenerator
# 2. Fills its values and saves this as the solved state
# 3. Removes the appropriate number of cells
# 4. Returns the representative 2D Python Lists of the board and solution
# Parameters:
# size is the number of rows/columns of the board (9 for this project)
# removed is the number of cells to clear (set to 0)
# Return: list[list] (a 2D Python list to represent the board)

def generate_sudoku(size, removed):
    global board1
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()

    rows = len(board)
    cols = len(board[0])
    for i in range(rows):
        for j in range(cols):
            board1[i][j] = board[i][j]

    sudoku.remove_cells()
    board = sudoku.get_board()
    return board
