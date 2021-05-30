import pygame

class Snake:
    color = (0, 255, 0)

    def __init__(self, x, y):
        self.cells = [Cell(x, y)]
        self.x = x
        self.y = y

    def addCell(self):
        self.cells.append(Cell())

    def draw(self, screen):
        for cell in self.cells:
            cell.draw(screen)




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

