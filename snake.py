import pygame

class Snake:
    color = (0, 255, 0)

    def __init__(self, x, y):
        self.cells = [Cell(x, y)]
        self.direction = 'LEFT'

    def draw(self, screen):
        for cell in self.cells:
            cell.draw(screen)

    def grow(self, x, y):
        self.cells.insert(0, Cell(x,y))

    def move(self, new_direction):
        if new_direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if new_direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if new_direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if new_direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        head = self.cells[0]
        previousX = head.x
        previousY = head.y

        if self.direction == 'UP':
            head.y -= Cell.height
        elif self.direction == 'LEFT':
            head.x -= Cell.width
        elif self.direction == 'RIGHT':
            head.x += Cell.width
        elif self.direction == 'DOWN':
            head.y += Cell.height

        for cell in self.cells:
            if cell == head:
                continue
            tempX = cell.x
            tempY = cell.y
            cell.x = previousX
            cell.y = previousY
            previousX = tempX
            previousY = tempY









class Cell:
    width = 20
    height = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, Snake.color, (self.x, self.y, Cell.width, Cell.height), 0)



class Food:
    color = (255, 0, 0)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, Food.color, (self.x, self.y, Cell.width, Cell.height), 0)

