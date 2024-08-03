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
from random import random
from components.common import Clickable, Drawable


class Wolf(Clickable, Drawable):
    def __init__(self, x, bottom, w=None, h=None):
        super().__init__()

        self.gameDisplay = pygame.display.get_surface()
        self.bottom = bottom
        self.on_click = None
        self.step = 0

        self.img_1 = utils.scale_image_maintain_ratio(
            config.images.get("wolf"),
            w=w, h=h
        )
        self.img_2 = utils.scale_image_maintain_ratio(
            config.images.get("wolf_idle"),
            w=w, h=h
        )

        self.set_image_rect(self.img_1, x,
                            self.bottom - self.img_1.get_height())

    def update(self):
        Clickable.update(self)
        Drawable.update(self)

        if self.step > 240:
            self.set_image_rect(self.img_2,
                                y=self.bottom - self.img_2.get_height())
        else:
            self.set_image_rect(self.img_1,
                                y=self.bottom - self.img_1.get_height())

        self.step += random() * 0.5
        if self.step > 300:
            self.step = 0
