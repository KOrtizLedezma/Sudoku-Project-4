import pygame
import sys
import board
import sudoku_generator


# Draws the Menu with all the buttons and deals with clicks
def draw_menu(screen1):
    # Dimensions for the buttons
    button_width = 150
    button_height = 50

    # Start Point for the buttons
    button_y = 800 - 250

    # Creation of the buttons
    button_easy = pygame.Rect(150, button_y, button_width, button_height)
    button_medium = pygame.Rect(325, button_y, button_width, button_height)
    button_hard = pygame.Rect(500, button_y, button_width, button_height)

    # Orange will contain the rgb code to make the code easy to read
    orange = (255, 79, 0)

    # Creation of the rectangle
    pygame.draw.rect(screen1, orange, button_easy)
    pygame.draw.rect(screen1, orange, button_medium)
    pygame.draw.rect(screen1, orange, button_hard)

    # We declare the fonts here so the code will be easy to read
    font = pygame.font.Font(None, 40)
    title_font = pygame.font.Font(None, 115)
    game_mode_font = pygame.font.Font(None, 65)

    # Creation of the labels that appear on the main menu
    title_text = title_font.render("Welcome to Sudoku", True, (0, 0, 0))
    title_rectangle = title_text.get_rect(center=(400, 150))
    screen1.blit(title_text, title_rectangle)

    game_mode_text = game_mode_font.render("Select Game Mode:", True, (0, 0, 0))
    game_mode_rectangle = game_mode_text.get_rect(center=(400, 400))
    screen1.blit(game_mode_text, game_mode_rectangle)

    # Creation of the texts for the buttons
    button_easy_text = font.render('EASY', True, (245, 245, 245))
    button_medium_text = font.render('MEDIUM', True, (245, 245, 245))
    button_hard_text = font.render('HARD', True, (245, 245, 245))

    # Format for the text
    text_easy = button_easy_text.get_rect(center=button_easy.center)
    text_medium = button_medium_text.get_rect(center=button_medium.center)
    text_hard = button_hard_text.get_rect(center=button_hard.center)

    screen1.blit(button_easy_text, text_easy)
    screen1.blit(button_medium_text, text_medium)
    screen1.blit(button_hard_text, text_hard)

    # Game Loop that will deal with the clicks on the buttons
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_easy.collidepoint(event.pos):
                    draw_game(difficulty='EASY')
                elif button_medium.collidepoint(event.pos):
                    draw_game(difficulty='MEDIUM')
                elif button_hard.collidepoint(event.pos):
                    draw_game(difficulty='HARD')
        pygame.display.update()


# Draws the game screen including the board and buttons, deals with clicks of the buttons
def draw_game(difficulty):
    # Initialization of pygame and the screen
    pygame.init()
    game_screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption(f'SUDOKU - {difficulty}')
    game_screen.fill((202, 228, 241))

    # Creation of the buttons
    button_reset = pygame.Rect(200, 700, 100, 25)
    button_restart = pygame.Rect(350, 700, 100, 25)
    button_exit = pygame.Rect(500, 700, 100, 25)

    # Orange will contain the rgb code to make the code easy to read
    orange = (255, 79, 0)

    # Creation of the rectangles for the buttons
    pygame.draw.rect(game_screen, orange, button_reset)
    pygame.draw.rect(game_screen, orange, button_restart)
    pygame.draw.rect(game_screen, orange, button_exit)

    font = pygame.font.Font(None, 28)

    # Texts for the buttons
    button_reset_text = font.render('RESET', True, (245, 245, 245))
    button_restart_text = font.render('RESTART', True, (245, 245, 245))
    button_exit_text = font.render('EXIT', True, (245, 245, 245))

    # Format for the texts
    text_reset = button_reset_text.get_rect(center=button_reset.center)
    text_restart = button_restart_text.get_rect(center=button_restart.center)
    text_exit = button_exit_text.get_rect(center=button_exit.center)

    game_screen.blit(button_reset_text, text_reset)
    game_screen.blit(button_restart_text, text_restart)
    game_screen.blit(button_exit_text, text_exit)

    # Declaration of the sudoku_generator class
    sudoku_class = sudoku_generator
    # Declaration of the variable board that it's going to contain the board
    board1 = None

    # Creation of 2 2D arrays filled with 0
    sketch_board = [['0' for _ in range(9)] for _ in range(9)]
    to_edit = [['0' for _ in range(9)] for _ in range(9)]

    # if and elif statements to see how many cells will be deleted, it will also draw the board on each statement
    if difficulty == 'EASY':
        original = sudoku_class.generate_sudoku(9, 30)
        for i in range(9):
            for j in range(9):
                to_edit[i][j] = original[i][j]

        solved_board = sudoku_class.board1
        board1 = board.Board(800, 800, game_screen, difficulty, original, to_edit, solved_board, sketch_board)
        board1.draw()
    elif difficulty == 'MEDIUM':
        original = sudoku_class.generate_sudoku(9, 40)
        for i in range(9):
            for j in range(9):
                to_edit[i][j] = original[i][j]
        solved_board = sudoku_class.board1
        board1 = board.Board(800, 800, game_screen, difficulty, original, to_edit, solved_board, sketch_board)
        board1.draw()
    if difficulty == 'HARD':
        original = sudoku_class.generate_sudoku(9, 50)
        for i in range(9):
            for j in range(9):
                to_edit[i][j] = original[i][j]
        solved_board = sudoku_class.board1
        board1 = board.Board(800, 800, game_screen, difficulty, original, to_edit, solved_board, sketch_board)
        board1.draw()

    # Game loop to check for clicks or inputs on the keyboard
    while True:

        for event in pygame.event.get():

            # To finish the program
            if event.type == pygame.QUIT:
                sys.exit()

            # To check if the user is pressing the ENTER key, this will move the sketched values to the final value
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                for i in range(9):
                    for j in range(9):
                        if board1.bool_board[i][j] == 1:
                            if board1.sketch_board[i][j] != '0':
                                board1.board_to_edit[i][j] = board1.sketch_board[i][j]
                                board1.sketch_board[i][j] = '0'
                                board1.draw()

                                if board1.is_full():
                                    if board1.check_board():
                                        draw_win()
                                    else:
                                        draw_lose(difficulty)

            # To check on the clicks on the screen,
            # It's going to get the col and row,
            # mark the selected cell and allow the user to change the value of the cell
            if event.type == pygame.MOUSEBUTTONDOWN:

                x, y = pygame.mouse.get_pos()
                if board1.select(x, y) is not None:
                    row, col = board1.select(x, y)

                    if board1.bool_board[col][row] != 0:

                        board1.mark_selected(row, col)
                        pygame.display.flip()
                        value = wait_for_key()
                        if value != 0:
                            board1.sketch_board[col][row] = str(value)
                            board1.draw()
                        else:
                            board1.sketch_board[col][row] = '0'
                            board1.board_to_edit[col][row] = 0
                            board1.draw()

                # Deals with the clicks on the reset button
                # Resets the board to its original state
                if button_reset.collidepoint(event.pos):
                    board1.reset_to_original()
                    board1.draw()

                # Restart the program
                elif button_restart.collidepoint(event.pos):
                    if __name__ == "__main__":
                        pygame.init()
                        screen_new = pygame.display.set_mode((800, 800))
                        pygame.display.set_caption('Sudoku')
                        background_image_new = pygame.image.load('Media/background.png')
                        screen_new.blit(background_image_new, (0, 0))
                        draw_menu(screen_new)
                # Deals with clicks on the exit button, it will quit the program
                elif button_exit.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()


# Draws the Winning screen
# It's going to deal with the click on the only button on the screen
def draw_win():
    pygame.init()
    win_screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Sudoku')

    background = pygame.image.load('Media/background.png')
    screen.blit(background, (0, 0))

    title_font = pygame.font.Font(None, 130)

    title_text = title_font.render("Game Won!", True, (0, 0, 0))
    title_rectangle = title_text.get_rect(center=(400, 250))
    win_screen.blit(title_text, title_rectangle)

    orange = (255, 79, 0)
    font = pygame.font.Font(None, 40)

    button_exit = pygame.Rect(300, 500, 200, 50)
    pygame.draw.rect(win_screen, orange, button_exit)
    button_exit_text = font.render('EXIT', True, (245, 245, 245))
    text_win = button_exit_text.get_rect(center=button_exit.center)
    win_screen.blit(button_exit_text, text_win)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_exit.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()


# Draws the Losing screen
# It's going to deal with the click on the only button on the screen
def draw_lose(difficulty):
    pygame.init()
    lose_screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Sudoku')

    background = pygame.image.load('Media/background.png')
    screen.blit(background, (0, 0))

    title_font = pygame.font.Font(None, 130)

    title_text = title_font.render("Game Over :(", True, (0, 0, 0))
    title_rectangle = title_text.get_rect(center=(400, 250))
    lose_screen.blit(title_text, title_rectangle)

    orange = (255, 79, 0)
    font = pygame.font.Font(None, 40)

    button_restart = pygame.Rect(300, 500, 200, 50)
    pygame.draw.rect(lose_screen, orange, button_restart)
    button_restart_text = font.render('RESTART', True, (245, 245, 245))
    text_restart = button_restart_text.get_rect(center=button_restart.center)
    lose_screen.blit(button_restart_text, text_restart)

    while True:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                sys.exit()
            if event1.type == pygame.MOUSEBUTTONDOWN:
                draw_game(difficulty)
        pygame.display.update()


# It is going to create a loop that won't be broken until the user inputs a value
# The valid inputs are going to be 1-9 and backspace keys
def wait_for_key():
    waiting = True
    num = 0

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            elif event.type == pygame.KEYDOWN and pygame.K_1 <= event.key <= pygame.K_9:
                num = event.key - pygame.K_0
                waiting = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                num = 0
                waiting = False

    return num


# Runs the program
if __name__ == "__main__":
    state = False
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Sudoku')

    background_image = pygame.image.load('Media/background.png')
    screen.blit(background_image, (0, 0))
    draw_menu(screen)
