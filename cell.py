import pygame.font


class Cell:

    # Constructor for the Cell class
    def __init__(self, value, row, col, screen, sketch=None):
        self.sketch = sketch
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

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

        cell_size = 100
        font = pygame.font.Font(None, 50)
        sketch_font = pygame.font.Font(None, 40)

        # Rectangle
        pygame.draw.rect(self.screen, (245, 245, 245),
                         ((self.col * cell_size), (self.row * cell_size), cell_size, cell_size))
        # Left Border
        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((self.col * cell_size), (self.row * cell_size), 2, cell_size))
        # Upper Border
        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((self.col * cell_size), (self.row * cell_size), cell_size, 2))
        # Right Border
        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((self.col * cell_size) + cell_size - 2, (self.row * cell_size), 2, cell_size))
        # Bottom Border
        pygame.draw.rect(self.screen, (0, 0, 0),
                         ((self.col * cell_size), (self.row * cell_size) + cell_size - 2, cell_size, 2))

        if self.value is not None:
            print('is not none')
            cell_value_text = font.render(self.value, True, (0, 0, 0))
            cell_value_text_rect = cell_value_text.get_rect(center=(
                (self.row * cell_size) + cell_size/2, (self.col * cell_size) + cell_size/2))
            self.screen.blit(cell_value_text, cell_value_text_rect)

        if self.sketch is not None:
            print('sketch')
            cell_sketch_text = sketch_font.render(self.value, True, (169, 169, 169))
            cell_sketch_text_rect = cell_sketch_text.get_rect(center=(
                (self.row * cell_size) + cell_size/10 + 10, (self.col * cell_size) + cell_size/10 + 10))
            self.screen.blit(cell_sketch_text, cell_sketch_text_rect)
