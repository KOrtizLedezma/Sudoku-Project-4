import pygame
import sys


def draw_menu(screen):

    button_width = 200
    button_height = 50

    button_y = 800 - 250

    button_easy = pygame.Rect(100, button_y, button_width, button_height)
    button_medium = pygame.Rect(400, button_y, button_width, button_height)
    button_hard = pygame.Rect(700, button_y, button_width, button_height)

    unselected = (255, 165, 0)

    pygame.draw.rect(screen, unselected, button_easy)
    pygame.draw.rect(screen, unselected, button_medium)
    pygame.draw.rect(screen, unselected, button_hard)

    font = pygame.font.Font(None, 32)
    title_font = pygame.font.Font(None, 130)
    game_mode_font = pygame.font.Font(None, 65)

    title_text = title_font.render("Welcome to Sudoku", True, (255, 165, 0))
    title_rectangle = title_text.get_rect(center=(500, 150))
    screen.blit(title_text, title_rectangle)

    game_mode_text = game_mode_font.render("Select Game Mode:", True, (255, 165, 0))
    game_mode_rectangle = game_mode_text.get_rect(center=(500, 400))
    screen.blit(game_mode_text, game_mode_rectangle)

    button_easy_text = font.render('Easy', True, (0, 0, 0))
    button_medium_text = font.render('Medium', True, (0, 0, 0))
    button_hard_text = font.render('Hard', True, (0, 0, 0))

    text_easy = button_easy_text.get_rect(center=button_easy.center)
    text_medium = button_medium_text.get_rect(center=button_medium.center)
    text_hard = button_hard_text.get_rect(center=button_hard.center)

    screen.blit(button_easy_text, text_easy)
    screen.blit(button_medium_text, text_medium)
    screen.blit(button_hard_text, text_hard)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_easy.collidepoint(event.pos):

                    print('Easy')
                elif button_medium.collidepoint(event.pos):
                    print('Medium')
                elif button_hard.collidepoint(event.pos):
                    print('Hard')
        pygame.display.update()


if __name__ == "__main__":
    state = False
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Sudoku')

    background_image = pygame.image.load('Media/background.png')
    screen.blit(background_image, (0, 0))

    draw_menu(screen)


