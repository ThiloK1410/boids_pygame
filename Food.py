import pygame
from Actor import Actor
import vector_manipulation as vec

class Food(Actor):
    def __init__(self, surface, x, y):
        sz, dx, dy = 20, 0, 0
        Actor.__init__(self, surface, x, y, sz, dx, dy)
        self.color = (34, 139, 34)

    def on_draw(self):
        pygame.draw.circle(self.my_surface, self.color, self.pos, self.size[0]/2)

    def move(self):     # Food will be able to move but only when forced
        self.pos = vec.add([self.pos, self.mov])
        self.mov = [0.0, 0.0]
