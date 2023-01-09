from Actor import Actor
import pygame


class Circle(Actor):
    def __init__(self, surface, x, y, sz=10, dx=0, dy=0):
        super().__init__(surface, x, y, sz, dx, dy)

    def on_draw(self):
        pygame.draw.circle(self.my_surface, self.color, self.pos, self.size[0]/2)
