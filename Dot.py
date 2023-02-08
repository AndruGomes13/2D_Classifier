############ Imports ############

import pygame

######## Base Dot Class ##########

class Dot:
    def __init__(self, x : int, y : int, color : tuple = pygame.Color("black")) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.radius = 10
    
    def coords(self):
        return (self.x, self.y)
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

d = Dot(10, 200, pygame.Color("white"))