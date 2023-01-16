import pygame
### Object Creation ###

class Dot:
    def __init__(self, x, y, color="black") -> None:
        self.x = x
        self.y = y
        self.radius = 10
        self._color = color
        self._color_code = color_dict[color]

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self._color_code = color_dict[value]

    @property
    def color_code(self):
        return self._color_code

    @color_code.setter
    def color_code(self, value):
        self._color_code = value
        self._color = f"Custom Color: {self._color_code}"

    def draw(self, win):
        pygame.draw.circle(win, self._color_code, (self.x, self.y), self.radius)

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

# Color Pallete
color_dict = {"white" : (255,255,255),
            "black" : (0, 0, 0),
            "grey" : (190, 190, 190),
            "red" : (255, 0, 0),
            }

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
 
                if event.button == 2:
                    color = "grey"
 
                print(color)
                mouse = pygame.mouse.get_pos()
                dot = Dot(mouse[0],mouse[1], color)
                dot_list.append(dot)
                print(f"Mouse coordinates: {mouse[0]} , {mouse[1]}")



        
        WIN.fill(color_dict["white"])
        for dot in dot_list:
            dot.draw(WIN)
        # pygame.draw.circle(WIN, color_dict["black"], (100, 100), 10)
        pygame.display.update()
    

    pygame.quit()












if __name__ == "__main__":
    main()