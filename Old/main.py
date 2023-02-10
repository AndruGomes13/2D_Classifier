""" Imports ################################################ """

import pygame
from Dot import *
from Button import *
import config

""" Variable Declaration ################################### """ 

# Constants ------------------------------------------------

# Window Display Size
WINDOW_WIDTH = 550
WINDOW_HEIGHT = 430
DISPLAY_DIM = (WINDOW_WIDTH, WINDOW_HEIGHT)
WIN = pygame.display.set_mode(DISPLAY_DIM)

# Frames per second
FPS = 60
CLOCK = pygame.time.Clock()

# Global Variables -----------------------------------------


# Creating window





# Initialize global project variables
pygame.init()
config.init()

# Dot list
dot_list    = []
button_list = []

color_select_button = StateMachineButton(10, 10, 100, 40, caption="Color", background_color="red", font_size=30, border_width= 3, border_radius= 3)
mode_button         = StateMachineButton(10, 10 + 50, 100, 40, caption="Place", background_color="black", font_size=30, font_color="grey", border_radius= 3)
run_sim_button      = StateMachineButton(10, 10 + 100, 100, 40, caption="Run", background_color="grey", font_size=30, border_radius= 3)

button_list.append(color_select_button)
button_list.append(mode_button)
button_list.append(run_sim_button)


def aux_workspace_additional_behaviour(self: WorkspaceButton, mouse_coord: tuple, event: Event, c: ProgramContext):
    
    # Check if it's in removal mode and there are any dots left
    if c.mode_button.state == False and len(c.dot_list) > 0:
        print("Removing Button!")

        # Find dot closest to the mouse
        selected_dot = get_closest_dot(mouse_coord)

        # Remove said dot
        remove_dot(c.dot)



if not self.state:
            if dot_list:
                print("remove")
                dot = get_closest_dot(mouse)
                remove_dot(dot)
                continue
            
            if color_select_button.state:
                add_dot(mouse, "red")

            if not color_select_button.state:
                add_dot(mouse, "green")


workspace = WorkspaceButton(120, 10, 400, 400, border_width = 3)
button_list.append(workspace)


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

def render(fnt, what, color, where):
    "Renders the fonts as passed from display_fps"
    text_to_show = fnt.render(what, 1, pygame.Color(color))
    WIN.blit(text_to_show, where)
 
 
def display_fps():
    "Data that will be rendered and blitted in _display"
    
    # Renders the FPS count at the corner of the screen
    render(
        pygame.font.SysFont("Arial", 20),
        what  = str(int(CLOCK.get_fps())),
        color = "green",
        where = (WINDOW_WIDTH - 50, 0))


def exit_program():
    pass

def mouse_button_down():
    pass


def main():
    """ Program Loop """
        
    CLOCK.tick(FPS)

    mouse_pos = pygame.mouse.get_pos()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            return

        # Interact with buttons
        for button in button_list:
            button.check_press(mouse_pos, event)

        if event.type == pygame.MOUSEBUTTONDOWN:

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
    display_fps()
    pygame.display.update()


if __name__ == "__main__":
    
    while True:
        main()
    
    pygame.quit()