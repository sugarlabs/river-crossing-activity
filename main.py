import pygame
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import config
from views import menu

class RiverCrossing:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

        self.gameDisplay = None
        self.info = None
        self.update_function = None
        self.bg = None

    def vw(self, x):
        return (x / 100) * self.display_rect.width

    def vh(self, y):
        return (y / 100) * self.display_rect.height

    def blit_centred(self, surf, x, y):
        rect = surf.get_rect()
        centered_coords = (x - rect.width // 2, y - rect.height // 2)
        self.gameDisplay.blit(surf, centered_coords)

    def stop(self):
        self.running = False

    def set_screen(self, view):
        view(self)

    def set_background(self, bg):
        w, h = bg.get_size()
        screen_w, screen_h = self.gameDisplay.get_size()
        m_w, m_h = w, h

        m_bg = bg

        if screen_w < w or screen_w > w:
            m_h = (h // w) * screen_w
            m_bg = pygame.transform.scale(
            bg, (screen_w, m_h))
            w, h = m_bg.get_size()
            m_w, m_h = w, h

        if screen_h > h:
            m_w = (w // h) * screen_h
            m_bg = pygame.transform.scale(m_w, screen_h)

        self.bg = m_bg


    def run(self):
        self.gameDisplay = pygame.display.get_surface()
        self.info = pygame.display.Info()
        self.display_rect = self.gameDisplay.get_rect()

        config.set_theme("default")
        self.set_screen(menu.view)

        if not (self.gameDisplay):
            self.gameDisplay = pygame.display.set_mode(
                (self.info.current_w, self.info.current_h))
            pygame.display.set_caption("River Crossing Puzzle")

        while self.running:
            self.gameDisplay.fill((2, 20, 20))
            
            if self.bg is not None:
                self.gameDisplay.blit(self.bg, (0, 0))

            while Gtk.events_pending():
                Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
            
            if self.update_function is not None:
                self.update_function()

            pygame.display.update()
            self.clock.tick(60)

        return


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = RiverCrossing()
    game.run()
