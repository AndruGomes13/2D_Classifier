import config
import pygame



class Dot:
    def __init__(self, x, y, color="black") -> None:
        self.x = x
        self.y = y
        self.radius = 4
        self._color = color
        self._color_code = config.color_dict[color]

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
        self._color_code = config.color_dict[value]

    @property
    def color_code(self):
        return self._color_code

    @color_code.setter
    def color_code(self, value):
        self._color_code = value
        self._color = f"Custom Color: {self._color_code}"

    def draw(self, win):
        pygame.draw.circle(win, self._color_code, (self.x, self.y), self.radius)

    def coords(self):
        return (self.x, self.y)