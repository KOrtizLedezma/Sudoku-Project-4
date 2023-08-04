import pygame
from cell import Cell
class Board:

    # Constructor for the Board class.
    # screen is a window from PyGame.
    # difficulty is a variable to indicate if the user chose easy, medium, or hard
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.current_selected = None
        self.board = [[Cell(0, row, col, self.screen) for col in range(self.width)] for row in range(self.height)]


    # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
    # Draws every cell on this board.
    def draw(self):
        cell_size = 100
        for row in range(self.height):
            for col in range(self.width):
                pygame.draw.rect(self.screen, (0, 0, 0),
                                 ((col * cell_size), (row * cell_size), cell_size, cell_size), 1)

                if (row % 3 == 0 or col % 3 == 0) and row > 0 and col > 0:
                    pygame.draw.rect(self.screen, (0, 0, 0),
                                     ((col * cell_size) - 2, (row * cell_size) - 2, cell_size + 4, cell_size + 4), 3)

        # Draw each cell
        for row in range(self.height):
            for col in range(self.width):
                cell = self.board[row][col]
                cell.draw()

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
        pass

    # Sets the sketched value of the current selected cell equal to user entered value.
    # It will be displayed at the top left corner of the cell using the draw() function.
    def sketch(self, value):
        row, col = self.current_selected
        cell = self.board[row][col]
        cell.set_sketched_value(value)

    # Sets the value of the current selected cell equal to user entered value.
    # Called when the user presses the Enter key.
    def place_number(self, value):
        pass

    # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)
    def reset_to_original(self):
        pass

    # Returns a Boolean value indicating whether the board is full or not.
    def is_full(self):
        pass

    # Updates the underlying 2D board with the values in all cells.
    def update_board(self):
        pass

    # Finds an empty cell and returns its row and col as a tuple
    def find_empty(self):
        pass

    # Check whether the Sudoku board is solved correctly.
    def check_board(self):
        pass
