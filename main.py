# Copyright (C) 2024 Spandan Barve
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame
import gi
from gi.repository import Gtk
import config
from views import menu
from components.help import Help


class RiverCrossing:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()

        self.gameDisplay = None
        self.info = None
        self.update_function = None
        self.bg = None

        self.help_popup = Help(self)

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
            m_h = (h / w) * screen_w
            m_bg = pygame.transform.scale(bg, (screen_w, int(m_h)))
            w, h = m_bg.get_size()
            m_w, m_h = w, h

        if screen_h > h:
            m_w = (w / h) * screen_h
            m_bg = pygame.transform.scale(bg, (int(m_w), screen_h))

        self.bg = m_bg

    def show_help(self):
        self.help_popup.show()

    def hide_help(self):
        self.help_popup.hide()

    def run(self):
        self.gameDisplay = pygame.display.get_surface()
        self.info = pygame.display.Info()
        self.display_rect = self.gameDisplay.get_rect()

        config.set_theme("default")
        self.set_screen(menu.view)
        self.help_popup.initialize()

        if not self.gameDisplay:
            self.gameDisplay = pygame.display.set_mode(
                (self.info.current_w, self.info.current_h))
            pygame.display.set_caption("River Crossing Puzzle")

        while self.running:
            self.gameDisplay.fill((2, 20, 20))

            if self.bg is not None:
                self.gameDisplay.blit(self.bg, (0, 0))

            if self.update_function is not None:
                self.update_function()

            while Gtk.events_pending():
                Gtk.main_iteration()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

            pygame.display.update()
            self.clock.tick(60)

        return


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = RiverCrossing()
    game.run()
