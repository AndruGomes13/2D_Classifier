import config
import pygame

class Button:
    def __init__(self, x, y, w, h, 
    font_color="black", 
    font_size = 30,
    caption ="", 
    background_color = "grey",
    border_width = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.limits = ((x, x + w),(y, y + h))
        self.caption = caption

        self._font_color = font_color
        self._font_color_code = config.color_dict[font_color]
        self.font_size = font_size

        self._background_color = background_color
        self._background_color_code = config.color_dict[background_color]

        self._background_color_code2 = config.color_dict["green"]
        self.border_width = border_width
        self.active = True

    ### Font color assignements ###    
    @property
    def font_color(self):
        return self._color

    @font_color.setter
    def font_color(self, value):
        self._color = value
        self._font_color_code = config.color_dict[value]

    @property
    def color_code(self):
        return self._font_color_code

    @color_code.setter
    def color_code(self, value):
        self._font_color_code = value
        self._color = f"Custom Color: {self._font_color_code}"

    ### Background color assignments

    @property
    def background_color(self):
        return self._background_color

    @background_color.setter
    def background_color(self, value):
        self._background_color = value
        self._background_color_code = config.color_dict[value]

    @property
    def background_color_code(self):
        return self._background_color_code

    @background_color_code.setter
    def background_color_code(self, value):
        self._background_color_code = value
        self._background_color = f"Custom Color: {self._background_color_code}"



    def draw(self, win):
        # Draw button
        button_rect = pygame.Rect(self.x, self.y, self.w, self.h)
        b_color = self._background_color_code if self.active else self._background_color_code2
        pygame.draw.rect(win, b_color, button_rect, self.border_width)
        
        # Draw caption
        font = pygame.font.Font(None, self.font_size)
        text = font.render(self.caption, True, self._font_color_code)
        rect_text = text.get_rect(center=(self.x + self.w // 2, self.y + self.h // 2))
        win.blit(text, rect_text)
        pass

    def check_press(self, mouse_coord):
        return (
            mouse_coord[0] > self.limits[0][0] and 
            mouse_coord[0] < self.limits[0][1] and
            mouse_coord[1] > self.limits[1][0] and
            mouse_coord[1] < self.limits[1][1])

