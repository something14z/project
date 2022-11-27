import pygame
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
COLORS = [WHITE, BLACK, GREEN, BLUE, RED]
class Rectangle():
    def __init__(self, left, top, size, rectcolor, figures):
        self.left = left
        self.top = top
        self.size = size
        self.color = rectcolor
        self.figures = figures
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.left, self.top, self.size, self.size))

    def change_color(self):
        self.color = COLORS[(COLORS.index(self.color) + 1) % len(COLORS)]


    def click(self, x, y):
        if x <= self.size + self.left and x >= self.left and y <= self.size + self.top and y >= self.top:

            self.draw()

    def cheskforclick (self, x, y, figures):
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.x, self.y = event.pos
                for rect in figures:
                    rect.click(x, y)

running = True
rectcolor = RED
pygame.init()
size = widht, height = (800, 600)
cellsize = 20
left = 150
top = 200
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
btn = []

for x in range(widht // cellsize):
    for y in range(height // cellsize):
        btn.append(Rectangle(x * cellsize, y * cellsize, cellsize, BLUE))
while running:
    for rect in btn:
        rect.draw()
        rect.checkforclick()

pygame.quit()
