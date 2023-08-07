import pygame
from cell import Cell


class Board:

    # Constructor for the Board class.
    # Screen is a window from PyGame.
    # Difficulty is a variable to indicate if the user chose easy, medium, or hard
    def __init__(self, width, height, screen, difficulty, board, board_to_edit, solved_board, sketch_board):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.current_selected = None
        self.board = board
        self.bool_board = self.generate_bool_list()
        self.sketch_board = sketch_board
        self.board_to_edit = board_to_edit
        self.solved_board = solved_board

    # Draws an outline of the Sudoku grid, with bold lines to delineate the 3x3 boxes.
    # Draws every cell on this board.
    def draw(self):
        for row in range(9):
            for col in range(9):
                cell = Cell(str(self.board_to_edit[row][col]), col + 1, row + 1, self.screen, self.bool_board[row][col],
                            self.sketch_board[row][col])
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
    # def select(self, x, y):
    #     row, col = self.click(x, y)
    #     if row is not None and col is not None:
    #         return row, col
    #     return None

    # If a tuple of (x, y) coordinates is within the displayed board, this function returns a tuple of the (row, col)
    # of the cell which was clicked. Otherwise, this function returns None.
    @staticmethod
    def select(x, y):
        if 140 <= x <= 670 and 65 <= y <= 595:
            row = ((x - 140) // 60)
            col = ((y - 65) // 60)
            return row, col
        else:
            return None

    def clear(self, x, y):
        row, col = self.select(x, y)
        if self.bool_board[row][col] == 1:
            self.board[row][col] = 0

    # Sets the sketched value of the current selected cell equal to user-entered value.
    # It will be displayed in the top left corner of the cell using the draw() function.
    def sketch(self, x, y):
        if self.select(x, y) is not None:
            row, col = self.select(x, y)
            sketched_value = input()
            self.sketch_board[row][col] = sketched_value

    # Sets the value of the current selected cell equal to the user entered value.
    # Called when the user presses the Enter key.
    def place_number(self, value, x, y):
        if self.select(x, y) is not None:
            row, col = self.select(x, y)
            if self.board_to_edit[row][col] == 0:
                self.board_to_edit[row][col] = value

    # Reset all cells in the board to their original values (0 if cleared, otherwise the corresponding digit)
    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                self.board_to_edit[row][col] = self.board[row][col]

    # Returns a Boolean value indicating whether the board is full or not.
    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.board_to_edit[row][col] == 0:
                    return False
        return True

    # Updates the underlying 2D board with the values in all cells.

    # Finds an empty cell and returns its row and col as a tuple
    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.board_to_edit[row][col] == 0:
                    return row, col
        return None

    # Check whether the Sudoku board is solved correctly.
    def check_board(self):
        for row in range(9):
            for col in range(9):
                if str(self.board_to_edit[row][col]) != str(self.solved_board[row][col]):
                    return False
        return True

    def generate_bool_list(self):
        # 0 meaning cant be edited
        # 1 meaning can be edited
        bool_list = [[-1 for _ in range(9)] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    bool_list[row][col] = 0
                else:
                    bool_list[row][col] = 1
        return bool_list

    def mark_selected(self, row, col):
        # Left Border
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (((row + 1) * 60 + 75), ((col + 1) * 60), 2, 60))
        # Upper Border
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (((row + 1) * 60 + 75), ((col + 1) * 60), 60, 2))
        # Right Border
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (((row + 1) * 60 + 75) + 60 - 2, ((col + 1) * 60), 2, 60))
        # Bottom Border
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (((row + 1) * 60 + 75), ((col + 1) * 60) + 60 - 2, 60, 2))
