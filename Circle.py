from Actor import Actor
import pygame


class Circle(Actor):
    kin = []
    avg_pos = [0.0, 0.0]

    def __init__(self, surface, x, y, dx=0, dy=0, sz=20):
        super().__init__(surface, x, y, sz, dx, dy)
        self.kin.append(self)
        self.flocking_strength = 0.001

    @classmethod
    def update_avg_pos(cls):
        sum_pos = [0.0, 0.0]
        for circle in cls.kin:
            sum_pos[0] += circle.pos[0]
            sum_pos[1] += circle.pos[1]
        cls.avg_pos[0] = sum_pos[0] / len(cls.kin)
        cls.avg_pos[1] = sum_pos[1] / len(cls.kin)

    def on_draw(self):
        pygame.draw.circle(self.my_surface, self.color, self.pos, self.size[0]/2)
