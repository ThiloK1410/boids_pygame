from Actor import Actor
import pygame
import vector_manipulation as vec


class Circle(Actor):
    kin = []
    avg_pos = [0.0, 0.0]

    def __init__(self, surface, x, y, dx=0, dy=0, sz=20):
        super().__init__(surface, x, y, sz, dx, dy)
        self.avg_pos = [self.screensize[0]/2, self.screensize[1]/2]
        self.kin.append(self)
        self.flocking_strength = 0.001

    @classmethod
    def update_avg_pos(cls):
        if len(cls.kin) > 0:
            kin_pos = []
            for i, circle in enumerate(cls.kin):
                kin_pos.append(circle.pos)
            sum_pos = vec.add(kin_pos)
            cls.avg_pos = vec.divide(sum_pos, len(kin_pos))

    def on_draw(self):
        pygame.draw.circle(self.my_surface, self.color, self.pos, self.size[0]/2)
