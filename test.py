import pygame, random, os

DISPLAY_DIM = (900, 500)

WIN = pygame.display.set_mode(DISPLAY_DIM)
pygame.display.set_caption("First Window")

WHITE = (255,255,255)

color_dict={"white": (255,255,255),
            "black": (0, 0, 0)}

FPS = 60

SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 30

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

VEL = 5

class Button:
    def __init__(self, x, y, w, h, caption="", color="black") -> None:
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.caption = caption
        self.color = color
        self.rect_obj = pygame.Rect(self.x, self.y, self.width, self.height)


    def check_click(self, mouse):
        pass


    def draw(self, win):
        pygame.draw.rect(win, color_dict[self.color], self.rect_obj)

class Spaceship:
    def __init__(self,x,y,color) -> None:
        self.x = x
        self.y = y
        self.color = color

yellow = Spaceship(100, 100, "yellow")
red = Spaceship(300, 300, "red")


def draw_window(yellow, red, button):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))
    button.draw(WIN)
    pygame.display.update()

def red_handle_movement(obj, keys_pressed):
    if keys_pressed[pygame.K_a]:
        obj.x -= VEL
    if keys_pressed[pygame.K_d]:
        obj.x += VEL
    if keys_pressed[pygame.K_w]:
        obj.y -= VEL
    if keys_pressed[pygame.K_s]:
        obj.y += VEL

def yellow_handle_movement(obj, keys_pressed):
    if keys_pressed[pygame.K_LEFT]:
        obj.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:
        obj.x += VEL
    if keys_pressed[pygame.K_UP]:
        obj.y -= VEL
    if keys_pressed[pygame.K_DOWN]:
        obj.y += VEL

b = Button(20, 20,50, 20)
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
       

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(yellow, keys_pressed)
        red_handle_movement(red, keys_pressed)

        draw_window(yellow, red, b)

    pygame.quit()


if __name__ == "__main__":
    main()