# -*- coding: utf-8 -*-
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
DARK_BLUE = (0,5,157)
LIGHT_GREEN = (111,255,109)
GREEN = (0, 255, 0)
DARK_GREEN = (0,102,2)
LIGHT_RED = (255, 111, 97)
RED = (255, 0, 0)
DARK_RED = (137, 2, 0)
LIGHT_CYAN = (0, 255, 255)
CYAN = (0, 133, 244)
DARK_CYAN = (0,65,132)
GREENISH_YELLOW = (181,255,14)
YELLOW = (255, 255, 0)
DARK_YELLOW = (168, 165, 0)
ORANGE = (255, 116, 3)
DARK_ORANGE = (143, 64, 0 )
PURPLE = (117, 0, 244)
DARK_PURPLE = (64, 0, 113)
PINK = (240, 0, 236)
DARK_PINK = (168, 0, 166)
BROWN = (150, 75, 0)
LIGHT_GRAY = (210, 210, 210)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

pygame.init()


janela = pygame.display.set_mode((700,670))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    janela.fill((WHITE))

    # desenhando na superfície
    pygame.draw.rect(janela, DARK_GREEN, [10, 5, 100, 100])
    pygame.draw.rect(janela, LIGHT_CYAN, [120, 5, 100, 100])
    pygame.draw.rect(janela, DARK_RED, [230, 5, 100, 100])
    pygame.draw.rect(janela, DARK_BLUE, [340, 5, 100, 100])
    pygame.draw.rect(janela, PURPLE, [450, 5, 100, 100])
    pygame.draw.rect(janela, LIGHT_GRAY, [560, 5, 100, 100])
    pygame.draw.rect(janela, PINK, [10, 115, 100, 100])
    pygame.draw.rect(janela, RED, [120, 115, 100, 100])
    pygame.draw.rect(janela, BLUE, [230, 115, 100, 100])
    pygame.draw.rect(janela, DARK_YELLOW, [340, 115, 100, 100])
    pygame.draw.rect(janela, DARK_ORANGE, [450, 115, 100, 100])
    pygame.draw.rect(janela, CYAN, [560, 115, 100, 100])
    pygame.draw.rect(janela, BLACK, [10, 225, 100, 100])
    pygame.draw.rect(janela, GRAY, [120, 225, 100, 100])
    pygame.draw.rect(janela, GREENISH_YELLOW, [230, 225, 100, 100])
    pygame.draw.rect(janela, CYAN, [340, 225, 100, 100])
    pygame.draw.rect(janela, DARK_BLUE, [450, 225, 100, 100])
    pygame.draw.rect(janela, LIGHT_GREEN, [560, 225, 100, 100])
    pygame.draw.rect(janela, DARK_PINK, [10, 335, 100, 100])
    pygame.draw.rect(janela, LIGHT_CYAN, [120, 335, 100, 100])
    pygame.draw.rect(janela, ORANGE, [230, 335, 100, 100])
    pygame.draw.rect(janela, DARK_RED, [340, 335, 100, 100])
    pygame.draw.rect(janela, PURPLE, [450, 335, 100, 100])
    pygame.draw.rect(janela, DARK_CYAN, [560, 335, 100, 100])
    pygame.draw.rect(janela, LIGHT_RED, [10, 445, 100, 100])
    pygame.draw.rect(janela, DARK_GRAY, [120, 445, 100, 100])
    pygame.draw.rect(janela, DARK_PURPLE, [230, 445, 100, 100])
    pygame.draw.rect(janela, DARK_YELLOW, [340, 445, 100, 100])
    pygame.draw.rect(janela, DARK_GREEN, [450, 445, 100, 100])
    pygame.draw.rect(janela, DARK_PINK, [560, 445, 100, 100])
    pygame.draw.rect(janela, BROWN, [10, 555, 100, 100])
    pygame.draw.rect(janela, GRAY, [120, 555, 100, 100])
    pygame.draw.rect(janela, PINK, [230, 555, 100, 100])
    pygame.draw.rect(janela, BLUE, [340, 555, 100, 100])
    pygame.draw.rect(janela, GREEN, [450, 555, 100, 100])
    pygame.draw.rect(janela, RED, [560, 555, 100, 100])



    pygame.display.flip()




