import pygame.font
from pygame import Rect


class Cell:

    # Constructor for the Cell class
    def __init__(self, value, row, col, screen, is_selected):
        self.sketch = '0'
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.is_selected = is_selected

    # Setter for this cell’s value
    def set_cell_value(self, value):
        self.value = value

    # Setter for this cell’s sketched value
    def set_sketched_value(self, value):
        self.sketch = value

    # Draws this cell, along with the value inside it.
    # If this cell has a nonzero value, that value is displayed.
    # Otherwise, no value is displayed in the cell.
    # The cell is outlined red if it is currently selected
    def draw(self):

        cell_size = 60
        font = pygame.font.Font(None, 50)
        sketch_font = pygame.font.Font(None, 25)

        # Rectangle
        pygame.draw.rect(self.screen, (245, 245, 245),
                         ((self.col * cell_size + 75), (self.row * cell_size), cell_size, cell_size))
        # Left Border
        pygame.draw.rect(self.screen, (128, 128, 128),
                         ((self.col * cell_size + 75), (self.row * cell_size), 2, cell_size))
        # Upper Border
        pygame.draw.rect(self.screen, (128, 128, 128),
                         ((self.col * cell_size + 75), (self.row * cell_size), cell_size, 2))
        # Right Border
        pygame.draw.rect(self.screen, (128, 128, 128),
                         ((self.col * cell_size + 75) + cell_size - 2, (self.row * cell_size), 2, cell_size))
        # Bottom Border
        pygame.draw.rect(self.screen, (128, 128, 128),
                         ((self.col * cell_size + 75), (self.row * cell_size) + cell_size - 2, cell_size, 2))

        if self.is_selected:
            # Left Border
            pygame.draw.rect(self.screen, (255, 0, 0),
                             ((self.col * cell_size + 75), (self.row * cell_size), 2, cell_size))
            # Upper Border
            pygame.draw.rect(self.screen, (255, 0, 0),
                             ((self.col * cell_size + 75), (self.row * cell_size), cell_size, 2))
            # Right Border
            pygame.draw.rect(self.screen, (255, 0, 0),
                             ((self.col * cell_size + 75) + cell_size - 2, (self.row * cell_size), 2, cell_size))
            # Bottom Border
            pygame.draw.rect(self.screen, (255, 0, 0),
                             ((self.col * cell_size + 75), (self.row * cell_size) + cell_size - 2, cell_size, 2))

        if self.sketch != '0':
            cell_sketch_text = sketch_font.render(self.sketch, True, (168, 168, 168))
            cell_sketch_text_rect = cell_sketch_text.get_rect(center=(
                (self.row * cell_size + 75) + cell_size / 10 + 5, (self.col * cell_size) + cell_size / 10 + 5))
            self.screen.blit(cell_sketch_text, cell_sketch_text_rect)

        if self.value != '0':
            cell_value_text = font.render(self.value, True, (0, 0, 0))
            cell_value_text_rect = cell_value_text.get_rect(center=(
                (self.row * cell_size + 75) + cell_size / 2, (self.col * cell_size) + cell_size / 2))
            self.screen.blit(cell_value_text, cell_value_text_rect)
