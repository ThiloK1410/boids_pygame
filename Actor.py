import pygame
import math


class Actor:
    population = []
    avg_pos = [0.0, 0.0]

    def __init__(self, surface, x, y, sz=10, dx=0.2, dy=-0.1, f_s=0):
        self.population.append(self)
        self.my_surface = surface
        self.color = (255, 0, 0)
        self.pos = [float(x), float(y)]
        self.mov = [dx, dy]
        self.size = [sz, sz]        # size should be quadratic
        self.screensize = [surface.get_width(), surface.get_height()]
        self.mx_speed = 20
        self.border_zone = 0.1
        self.border_push_force = 0.5      # TODO: maybe change border_zone or push_force in relation to mx_speed
        self.border_zone_abs = [int(self.screensize[0]*self.border_zone), int(self.screensize[1]*self.border_zone)]
        self.flocking_strength = f_s

    @classmethod
    def get_len(cls, direction):
        temp = 0
        for x in direction:
            temp += x*x
        return math.sqrt(temp)

    @classmethod
    def has_same_sign(cls, x, y):
        if x == 0:
            if y == 0:
                return True
            return False
        if y == 0:
            return False
        if x/abs(x) == y/abs(y):
            return True
        return False

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
        speed = math.sqrt(self.get_len(self.mov))
        if speed > mx_speed:
            factor = mx_speed/speed
            self.mov[0] *= factor
            self.mov[1] *= factor

    def flock(self):
        if not self.flocking_strength == 0:
            flock_dir = [0.0, 0.0]
            flock_dir[0] = self.avg_pos[0] - self.pos[0]
            flock_dir[1] = self.avg_pos[1] - self.pos[1]
            if self.get_len(self.pos) > 50:
                self.mov[0] += self.flocking_strength*flock_dir[0]
                self.mov[1] += self.flocking_strength*flock_dir[1]

    def collision(self):
        for x in self.population:
            if not x == self:
                distance = [0.0, 0.0]
                distance[0] = x.pos[0] - self.pos[0]
                distance[1] = x.pos[1] - self.pos[1]
                distance_abs = self.get_len(distance)
                if distance_abs < (self.size[0] + x.size[0])/2 and not distance_abs == 0:
                    if self.has_same_sign(self.mov[0], distance[0]):
                        self.mov[0] -= distance[0] / distance_abs
                    if self.has_same_sign(self.mov[1], distance[1]):
                        self.mov[1] -= distance[1] / distance_abs
                    if not self.has_same_sign(x.mov[0], distance[0]):
                        x.mov[0] += distance[0] / distance_abs
                    if not self.has_same_sign(x.mov[1], distance[1]):
                        x.mov[1] += distance[1] / distance_abs

    def move(self):
        self.pos[0] += self.mov[0]
        self.pos[1] += self.mov[1]

        # function which will be externally called every tick
    def on_step(self):
        self.set_max_speed(self.mx_speed)
        self.push_to_center()
        self.flock()
        self.collision()
        self.move()
        self.on_draw()

