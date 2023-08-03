import pygame
import sys


def draw_menu(screen1):

    button_width = 150
    button_height = 50

    button_y = 800 - 250

    button_easy = pygame.Rect(150, button_y, button_width, button_height)
    button_medium = pygame.Rect(325, button_y, button_width, button_height)
    button_hard = pygame.Rect(500, button_y, button_width, button_height)

    orange = (255, 79, 0)

    pygame.draw.rect(screen1, orange, button_easy)
    pygame.draw.rect(screen1, orange, button_medium)
    pygame.draw.rect(screen1, orange, button_hard)

    font = pygame.font.Font(None, 40)
    title_font = pygame.font.Font(None, 115)
    game_mode_font = pygame.font.Font(None, 65)

    title_text = title_font.render("Welcome to Sudoku", True, (0, 0, 0))
    title_rectangle = title_text.get_rect(center=(400, 150))
    screen1.blit(title_text, title_rectangle)

    game_mode_text = game_mode_font.render("Select Game Mode:", True, (0, 0, 0))
    game_mode_rectangle = game_mode_text.get_rect(center=(400, 400))
    screen1.blit(game_mode_text, game_mode_rectangle)

    button_easy_text = font.render('EASY', True, (245, 245, 245))
    button_medium_text = font.render('MEDIUM', True, (245, 245, 245))
    button_hard_text = font.render('HARD', True, (245, 245, 245))

    text_easy = button_easy_text.get_rect(center=button_easy.center)
    text_medium = button_medium_text.get_rect(center=button_medium.center)
    text_hard = button_hard_text.get_rect(center=button_hard.center)

    screen1.blit(button_easy_text, text_easy)
    screen1.blit(button_medium_text, text_medium)
    screen1.blit(button_hard_text, text_hard)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_easy.collidepoint(event.pos):
                    draw_game(difficulty='EASY')
                    print('Easy')
                elif button_medium.collidepoint(event.pos):
                    draw_game(difficulty='MEDIUM')
                    print('Medium')
                elif button_hard.collidepoint(event.pos):
                    draw_game(difficulty='HARD')
                    print('Hard')
        pygame.display.update()


def draw_game(difficulty):
    pygame.init()
    game_screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption(f'SUDOKU - {difficulty}')
    game_screen.fill((202, 228, 241))

    button_reset = pygame.Rect(200, 700, 100, 25)
    button_restart = pygame.Rect(350, 700, 100, 25)
    button_exit = pygame.Rect(500, 700, 100, 25)

    orange = (255, 79, 0)

    pygame.draw.rect(game_screen, orange, button_reset)
    pygame.draw.rect(game_screen, orange, button_restart)
    pygame.draw.rect(game_screen, orange, button_exit)

    font = pygame.font.Font(None, 28)

    button_reset_text = font.render('RESET', True, (245, 245, 245))
    button_restart_text = font.render('RESTART', True, (245, 245, 245))
    button_exit_text = font.render('EXIT', True, (245, 245, 245))

    text_reset = button_reset_text.get_rect(center=button_reset.center)
    text_restart = button_restart_text.get_rect(center=button_restart.center)
    text_exit = button_exit_text.get_rect(center=button_exit.center)

    game_screen.blit(button_reset_text, text_reset)
    game_screen.blit(button_restart_text, text_restart)
    game_screen.blit(button_exit_text, text_exit)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_reset.collidepoint(event.pos):
                    pass
                elif button_restart.collidepoint(event.pos):
                    pass
                elif button_exit.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()


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


def draw_lose():
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_restart.collidepoint(event.pos):
                    sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    state = False
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Sudoku')

    background_image = pygame.image.load('Media/background.png')
    screen.blit(background_image, (0, 0))

    draw_menu(screen)
