import pygame
import math


class Actor:

    def __init__(self, surface, x, y, sz=10, dx=0.2, dy=-0.1):
        self.my_surface = surface
        self.pos = [x, y]
        self.mov = [dx, dy]
        self.size = [sz, sz]
        self.screensize = [surface.get_width(), surface.get_height()]
        self.mx_speed = 10
        self.border_zone = 0.05
        self.border_push_force = 0.01
        self.border_zone_abs = [int(self.screensize[0]*self.border_zone), int(self.screensize[1]*self.border_zone)]
        self.color = (255, 0, 0)

        # function which will be externally called every tick
    def on_draw(self):
        body = pygame.Rect(self.pos, self.size)
        pygame.draw.rect(self.my_surface, self.color, body)

        # checking all 4 sides of the screen, if Actor is to close he will get pushed away
    def push_to_center(self):
        if self.pos[0] < self.border_zone_abs[0]:
            self.mov[0] += self.border_push_force
        elif self.pos[0] > self.screensize[0] - self.border_zone_abs[0]:
            self.mov[0] -= self.border_push_force
        if self.pos[1] < self.border_zone_abs[1]:
            self.mov[1] += self.border_push_force
        elif self.pos[1] > self.screensize[1] - self.border_zone_abs[1]:
            self.mov[1] -= self.border_push_force

    def set_max_speed(self, mx_speed):
        speed = math.sqrt(self.mov[0]**2+self.mov[1]**2)
        if speed > mx_speed:
            factor = mx_speed/speed
            self.mov[0] *= factor
            self.mov[1] *= factor

    def move(self):
        self.pos[0] += self.mov[0]
        self.pos[1] += self.mov[1]

    def on_step(self):
        self.on_draw()
        self.push_to_center()
        self.set_max_speed(self.mx_speed)
        print(self.mov)
        self.move()
