import pygame
from snake import Snake

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Snake')

white = (255,255,255)

snake = Snake(400, 300)

game_over = False

snake.grow(420, 300)
snake.grow(440, 300)


def readKey(key):
    change_to = ''
    if key == pygame.K_UP or key == ord('w'):
        change_to = 'UP'
    if key == pygame.K_DOWN or key == ord('s'):
        change_to = 'DOWN'
    if key == pygame.K_LEFT or key == ord('a'):
        change_to = 'LEFT'
    if key == pygame.K_RIGHT or key == ord('d'):
        change_to = 'RIGHT'
    return change_to


while not game_over:
    change_to = snake.direction
    for event in pygame.event.get():
        game_over = event.type == pygame.QUIT;
        if event.type == pygame.KEYDOWN:
            change_to = readKey(event.key)



    screen.fill(white)

    snake.move(change_to)
    snake.draw(screen)

    msElapsed = clock.tick(10)


    pygame.display.update()






pygame.quit()
quit()


