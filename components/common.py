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
import utils


class Clickable:
    def __init__(self):
        self.press = False
        self.on_click = None
        self.rect = None

    def hovered(self):
        if self.rect is not None:
            return self.rect.collidepoint(pygame.mouse.get_pos())
        return False

    def update(self):
        pressed_btn = pygame.mouse.get_pressed()[0]
        if self.on_click is not None and self.press:
            if self.hovered() and pressed_btn != 1:
                self.on_click()

        if self.hovered() and pressed_btn == 1:
            self.press = True
        else:
            self.press = False


class Drawable:
    def __init__(self):
        self.gameDisplay = None
        self.image = None
        self.rect = None
        self.x = 0
        self.y = 0

    def set_image_rect(self, image, x=None, y=None, scale=1):
        w, h = image.get_size()
        self.image = pygame.transform.scale(image,
                                            (int(w * scale), int(h * scale)))

        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

        self.rect = self.image.get_rect()
        self.rect.x = self.x - ((scale - 1) * w) // 2
        self.rect.y = self.y - ((scale - 1) * h) // 2

    def draw(self):
        if utils.array_has_no_none([self.rect, self.gameDisplay]):
            self.gameDisplay.blit(self.image, self.rect)

    def update(self):
        if self.image is not None:
            self.draw()
