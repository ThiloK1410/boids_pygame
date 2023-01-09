
import pygame
from pygame.locals import *
from Circle import *


class App:
    def __init__(self):
        self.actors = None
        self.colors = {"RED": (255, 0, 0), "YELLOW": (255, 255, 0)}
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 800, 800

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.actors = [Actor(self._display_surf, 200, 200), Circle(self._display_surf, 300, 300)]

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

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
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
