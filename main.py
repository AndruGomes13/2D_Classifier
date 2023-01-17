import pygame
from Dot import *
from Button import *
import config

### Variable Declaration ###

# Creating window
DISPLAY_DIM = (550, 430)
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

color_select_button = Button(10, 10, 100, 40, caption="Color", background_color="red", font_size=30, border_width= 3, border_radius= 3)
mode_button = Button(10, 10 + 50, 100, 40, caption="Place", background_color="black", font_size=30, font_color="grey", border_radius= 3)
run_sim_button = Button(10, 10 + 100, 100, 40, caption="Run", background_color="grey", font_size=30, border_radius= 3)

button_list.append(color_select_button)
button_list.append(mode_button)
button_list.append(run_sim_button)

workspace = Button(120, 10, 400, 400, border_width = 3)


def add_dot(coord, color):
    dot = Dot(coord[0],coord[1], color)
    dot_list.append(dot)

def remove_dot(dot):
    dot_list.remove(dot)

def get_closest_dot(mouse):
    def dist_squared(dot1, dot2):
        return (dot1[0] - dot2[0])**2 + (dot1[1] - dot2[1])**2
    c_dot = []

    for dot in dot_list:
        if c_dot == []:
            c_dot = [dot, dist_squared(mouse, dot.coords())]
            continue
        dist = dist_squared(mouse, dot.coords())
        if dist < c_dot[1]:
            c_dot[0] = dot
            c_dot[1] = dist

    return c_dot[0]



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
                    if color_select_button.check_press(mouse):
                        color_select_button.state ^= 1

                    if mode_button.check_press(mouse):
                        mode_button.state ^= 1

                    if run_sim_button.check_press(mouse):
                        run_sim_button.state ^= 1


                    # Checks if click is inside the workspace
                    if workspace.check_press(mouse):
                        if not mode_button.state:
                            if dot_list:
                                print("remove")
                                dot = get_closest_dot(mouse)
                                remove_dot(dot)
                            continue
                        if color_select_button.state:
                            add_dot(mouse, "red")

                        if not color_select_button.state:
                            add_dot(mouse, "green")

                        

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