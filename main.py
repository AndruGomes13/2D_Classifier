import pygame
from Dot import *
import config
### Object Creation ###


class Button:
    def __init__(self) -> None:
        pass


### Variable Declaration ###

# Creating window
DISPLAY_DIM = (500, 500)
WIN = pygame.display.set_mode(DISPLAY_DIM)

# Frame-rate set
FPS = 60
clock = pygame.time.Clock()

# Initialize global project variables
config.init()

# Dot list
dot_list = []

def main():
    # Frame-rate set
    FPS = 60
    clock = pygame.time.Clock()
    ### Program Loop ###
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event)
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    color = "red"
                if event.button == 3:
                    color = "black"

                mouse = pygame.mouse.get_pos()
                dot = Dot(mouse[0],mouse[1], color)
                dot_list.append(dot)
  



        
        WIN.fill(config.color_dict["white"])
        for dot in dot_list:
            dot.draw(WIN)
        pygame.display.update()
    

    pygame.quit()












if __name__ == "__main__":
    main()