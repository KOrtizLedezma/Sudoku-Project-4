import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator


class Board:

    # Constructor for the Board class.
    # Screen is a window from PyGame.
    # Difficulty is a variable to indicate if the user chose easy, medium, or hard
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.current_selected = None
        self.cells = []

    # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
    # Draws every cell on this board.
    def draw(self):
        for row in range(9):
            for col in range(9):
                cell = Cell('0', row + 1, col + 1, self.screen, False)
                self.cells.append(cell)
                cell.draw()

        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((1 * 60 + 75), (1 * 60), 6, 540))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((4 * 60 + 75 - 3), (1 * 60), 6, 540))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((7 * 60 + 75 - 3), (1 * 60), 6, 540))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((10 * 60 + 75 - 3), (1 * 60 - 3), 6, 546))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((1 * 60 + 75), (1 * 60 - 3), 540, 6))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((1 * 60 + 75), (4 * 60 - 3), 540, 6))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((1 * 60 + 75), (7 * 60 - 3), 540, 6))
        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((1 * 60 + 75), (10 * 60 - 3), 540, 6))

    # Marks the cell at (row, col) in the board as the current selected cell.
    # Once a cell has been selected, the user can edit its value or sketched value.
    def select(self, row, col):
        self.current_selected = (row, col)

    # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
    # of the cell which was clicked. Otherwise, this function returns None.
    def click(self, x, y):
        cell_size = 100
        row, col = y // cell_size, x // cell_size
        if row < self.height and col < self.width:
            return row, col
        return None

    # Clears the value cell. Note that the user can only remove the cell values and sketched value that are
    # filled by themselves.
    def clear(self, value):
        if self.current_selected is not None:
            row, col = self.current_selected
            cell = self.cells[row][col]
            if cell.value == value:
                cell.set_cell_value(None)
                cell.set_sketched_value(None)
                cell.draw()

    # Sets the sketched value of the current selected cell equal to user-entered value.
    # It will be displayed in the top left corner of the cell using the draw() function.
    def sketch(self, value):
        if self.current_selected is not None:
            row, col = self.current_selected
            cell = self.cells[row][col]
            cell.set_sketched_value(value)
            cell.draw()

    # Sets the value of the current selected cell equal to user entered value.
    # Called when the user presses the Enter key.
    def place_number(self, value):
        board = SudokuGenerator.get_board()
        row, col = self.current_selected
        cell = board[row][col]
        cell.set_cell_value(value)

    # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)
    def reset_to_original(self):
        board = SudokuGenerator.get_board()
        for row in range(self.height):
            for col in range(self.width):
                cell = board[row][col]
                # cell.
                # where to find original value
        pass

    # Returns a Boolean value indicating whether the board is full or not.
    def is_full(self):
        board = SudokuGenerator.get_board()
        count = 0
        for row in range(self.height):
            for col in range(self.width):
                cell = board[row][col]
                if cell == 0:  # should I be comparing cell to 0 or call a funtion from Cell class
                    count += 1  # where to get value of that function
        if count == 0:
            return True

        pass

    # Updates the underlying 2D board with the values in all cells.
    def update_board(self):
        board = SudokuGenerator.get_board()
        for row in range(self.height):
            for col in range(self.width):
                cell = board[row][col]
                cell.set_cell_value()
        pass

    # Finds an empty cell and returns its row and col as a tuple
    def find_empty(self):
        board = SudokuGenerator.get_board()
        for row in range(self.height):
            for col in range(self.width):
                cell = board[row][col]
                if cell == 0:
                    return row, col
        pass

    # Check whether the Sudoku board is solved correctly.
    def check_board(self):
        pass
