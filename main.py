import pygame
from snake import Snake

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


pygame.init()
screen = pygame.display.set_mode((800, 600))

# pygame.display.update()
pygame.display.set_caption('Snake')

white = (255,255,255)

snake = Snake(400, 300)

game_over = False
while not game_over:
    for event in pygame.event.get():
        game_over = event.type == pygame.QUIT;
        if event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
        # print(event)  # prints out all the actions that take place on the screen

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    screen.fill(white)

    snake.draw(screen)


    snake.update()


    pygame.display.update()






pygame.quit()
quit()
