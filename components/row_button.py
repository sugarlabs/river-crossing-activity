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


import config
import utils
import pygame
from components.common import Clickable, Drawable


class RowButton(Clickable, Drawable):
    def __init__(self, x, y, w=None, h=None):
        super().__init__()

        self.gameDisplay = pygame.display.get_surface()

        image = config.images.get("arrow")
        self.img = utils.scale_image_maintain_ratio(image, w=w, h=h)
        self.set_image_rect(self.img, x, y)
        self.direction = "left"

        self.scale_factor = 0.1

    def flip(self):
        self.img = pygame.transform.flip(self.img, True, False)

    def update(self):
        Drawable.update(self)
        Clickable.update(self)

        if self.hovered():
            self.set_image_rect(self.img, scale=1 + self.scale_factor)
        else:
            self.set_image_rect(self.img, scale=1)
