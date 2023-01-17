import pygame
from Dot import *
from Button import *
import config

### Variable Declaration ###

# Creating window
DISPLAY_DIM = (600, 450)
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
button_list = []

button1 = Button(10, 10, 100, 40, caption="Color", background_color="red", font_size=30, border_width= 3)
button2 = Button(10, 10 + 50, 100, 40, caption="Place", background_color="black", font_size=30, font_color="grey")
button3 = Button(10, 10 + 100, 100, 40, caption="Run", background_color="grey", font_size=30, border_radius= 8)
button_list.append(button1)
button_list.append(button2)
button_list.append(button3)
workspace = Button(130, 10, 400, 400, border_width = 3)


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
                    if button1.check_press(mouse):
                        button1.active ^= 1

                    if button2.check_press(mouse):
                        button2.active ^= 1

                    if button3.check_press(mouse):
                        button3.active ^= 1

                    if workspace.check_press(mouse):
                        if button1.active:
                            color = "red"
                            dot = Dot(mouse[0],mouse[1], color)
                            dot_list.append(dot)

                        if not button1.active:
                            color = "green"
                            dot = Dot(mouse[0],mouse[1], color)
                            dot_list.append(dot)
            if event.type == pygame.MOUSEMOTION:
                pass



  



        
        WIN.fill(config.color_dict["white"])
        for dot in dot_list:
            dot.draw(WIN)

        for button in button_list:
            button.draw(WIN)
        workspace.draw(WIN)
        pygame.display.update()
    

    pygame.quit()












if __name__ == "__main__":
    main()