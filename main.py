import pygame
from Dot import *
from Button import *
import config

### Variable Declaration ###

# Creating window
DISPLAY_DIM = (500, 500)
WIN = pygame.display.set_mode(DISPLAY_DIM)
pygame.display.set_caption('Show Text')

# Frame-rate set
FPS = 60
clock = pygame.time.Clock()

# Initialize global project variables
pygame.init()
config.init()

# Dot list
dot_list = []

button = Button(10, 200, 100, 100, caption="Test", background_color="red", font_size=30)


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
                mouse = pygame.mouse.get_pos()
                if event.button == 1:
                    color = "red"
                    dot = Dot(mouse[0],mouse[1], color)
                    dot_list.append(dot)
                if event.button == 3:
                    color = "black"
                    dot = Dot(mouse[0],mouse[1], color)
                    dot_list.append(dot)
                if event.button == 2 and button.check_press(mouse):
                    print("clicked")


  



        
        WIN.fill(config.color_dict["white"])
        for dot in dot_list:
            dot.draw(WIN)
        button.draw(WIN)
        pygame.display.update()
    

    pygame.quit()












if __name__ == "__main__":
    main()