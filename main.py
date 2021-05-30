import pygame
from snake import Snake
from snake import Food

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Snake')

white = (255,255,255)
black = (0,0,0)

snake = Snake(440, 300)

game_over = False

snake.grow(420, 300)
snake.grow(400, 300)

# snake.printSnake()

score = 0

font = pygame.font.SysFont(None, 48)

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

food = None

while not game_over:
    change_to = snake.direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        # game_over = event.type == pygame.QUIT
        if event.type == pygame.KEYDOWN:
            change_to = readKey(event.key)



    screen.fill(white)

    if food == None:
        food = Food.generateFood(snake)

    if snake.eat(food):
        score += 1
        food = None

    if not food == None:
        food.draw(screen)


    snake.move(change_to)

    # print(snake.collidesintoitself())

    # snake.printSnake()

    game_over = snake.outofbounds(0, 800, 0, 600) or snake.collidesintoitself()
    snake.draw(screen)

    # img = font.render(str(score), True, black)
    # screen.blit(img, (400, 50))

    scoreText = font.render(str(score), True, black)
    scoreRect = scoreText.get_rect(center=(400, 50))
    screen.blit(scoreText, scoreRect)

    msElapsed = clock.tick(12)


    pygame.display.update()

i = 0
while True:
    if i % 2 == 0:
        color = black
        screen.fill(white)
    else:
        color = white
        screen.fill(black)
    scoreText = font.render(str(score), True, color)
    scoreRect = scoreText.get_rect(center=(400,50))
    screen.blit(scoreText, scoreRect)

    gameoverText = font.render("GAMEOVER", True, color)
    gameoverRect = gameoverText.get_rect(center=(800 / 2, 600 / 2))
    screen.blit(gameoverText, gameoverRect)
    pygame.display.update()
    msElapsed = clock.tick(8)
    i += 1
    if i > 5:
        break


pygame.quit()
quit()


