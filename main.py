import random
import pygame
from pygame.locals import *
from Circle import *
from Food import *


class App:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.actors = []
        self.colors = {"RED": (255, 0, 0), "YELLOW": (255, 255, 0)}
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1200, 800

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.actors = [Circle(self._display_surf, 300, 300, 8, 4), Circle(self._display_surf, 300, 300, 4, 8)]

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ran_pos = [random.randint(0, self.size[0]), random.randint(0, self.size[1])]
                self.actors.append(Circle(self._display_surf, *ran_pos, 8, 4))
            if event.key == pygame.K_b:
                ran_pos = [random.randint(0, self.size[0]), random.randint(0, self.size[1])]
                self.actors.append(Food(self._display_surf, *ran_pos))

    def on_loop(self):
        Circle.update_avg_pos()     # updates average position for Circle Class so flocking is possible

    def on_render(self):
        self._display_surf.fill(self.colors.get("YELLOW"))                  # DRAWS BACKGROUND
        for actor in self.actors:                                           # DRAWS ACTORS
            actor.on_step()
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()
            self.clock.tick(self.fps)
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
