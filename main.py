############### Imports ################

import pygame
from Buttons import *
from Dot import *
from pygame.event import Event
# import config

############### Variable Declaration ###########

# --------------- Constants -----------------

# Window Size
WINDOW_WIDTH = 550
WINDOW_HEIGHT = 450
DISPLAY_DIM = (WINDOW_WIDTH, WINDOW_HEIGHT)

# Creating Window
WIN = pygame.display.set_mode(DISPLAY_DIM)
pygame.display.set_caption('Algorithm Demo')

# Frames per second
FPS = 60
CLOCK = pygame.time.Clock()


# --------------- Global Variables ------------

# Initialize global project variables
pygame.init()
# config.init()


# Object list
dot_list = []

########## Auxiliary functions ##########

# Adds dot
def add_dot(coordinates: tuple, color: "string" ) -> None:
    dot = Dot(coordinates[0], coordinates[1], color)
    dot_list.append(dot)

# Handles mouse clicks (Adding and removing dots)
def click_handling(event: Event, mouse_pos : tuple) -> None:
    if event.button == 1:
        add_dot(mouse_pos, "red")

    if event.button == 3:
        add_dot(mouse_pos, "blue")

# Handles key presses (Mode changes)
def key_handling(event: Event) -> None:
    if event.key == pygame.K_a:
        print("a")

    


########## Main ##########
def main():
    
    # Setting FPS
    CLOCK.tick(FPS)

    # Getting Mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "quit"
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_handling(event, mouse_pos)

        if event.type == pygame.KEYDOWN:
            key_handling(event)

    

    ######### Rendering ###########
    WIN.fill(pygame.Color("white"))

    # Rendering dots
    for dot in dot_list:
        dot.draw(WIN)




    # Update display
    pygame.display.update()


    





if __name__ == "__main__":
    while True:
        status = main()

        # Handling app status
        if status == "quit":
            break

    pygame.quit()