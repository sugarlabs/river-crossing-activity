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
import config
import utils
from components.common import Clickable


class Boat(Clickable):
    def __init__(self, left_x, right_x, bottom, w):
        super().__init__()

        self.gameDisplay = pygame.display.get_surface()

        boat = config.images.get("boat")
        farmer = config.images.get("farmer")

        self.boat = utils.scale_image_maintain_ratio(boat, w=w)
        self.farmer = utils.scale_image_maintain_ratio(farmer, w=w // 3)

        self.boat_w = self.boat.get_width()
        self.boat_h = self.boat.get_height()

        self.farmer_w = self.farmer.get_width()
        self.farmer_h = self.farmer.get_height()

        self.left_x = left_x
        self.right_x = right_x
        self.x = self.left_x
        self.y = bottom - self.boat_h // 2

        self.holding = None
        self.holding_w = None
        self.holding_h = None

        self.row_callback = None
        self.position = "left"
        self.moving = False
        self.speed = 3

    def hold(self, image):
        if image is None:
            self.holding = None
            return
        self.holding = utils.scale_image_maintain_ratio(image,
                                                        h=self.farmer_h // 2)
        self.holding_w, self.holding_h = self.holding.get_size()

    def draw(self):
        farmer_x = 0
        if (self.position == "right" and self.moving) or (self.position == "left" and not self.moving):
            farmer_x = self.x + self.boat_w * 0.1
        if (self.position == "left" and self.moving) or (self.position == "right" and not self.moving):
            farmer_x = self.x + self.boat_w * 0.9 - self.farmer_w

        farmer_y = self.y - self.farmer_h * 0.6
        self.gameDisplay.blit(self.farmer, (int(farmer_x), int(farmer_y)))

        if self.holding is not None:
            holding_x = 0
            if (self.position == "left" and self.moving) or (self.position == "right" and not self.moving):
                holding_x = self.x + self.boat_w * 0.1
            if (self.position == "right" and self.moving) or (self.position == "left" and not self.moving):
                holding_x = self.x + self.boat_w * 0.9 - self.holding_w

            holding_y = self.y - self.holding_h * 0.5
            self.gameDisplay.blit(self.holding,
                                  (int(holding_x),
                                   int(holding_y)))

        self.gameDisplay.blit(self.boat, (self.x, self.y))

    def row(self, callback=None):
        if self.moving:
            return

        if self.position == "left":
            self.position = "right"
        elif self.position == "right":
            self.position = "left"

        self.row_callback = callback

    def update(self):
        Clickable.update(self)
        self.rect = self.boat.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        if self.position == "right" and self.x < self.right_x:
            self.moving = True
            self.x += self.speed
        elif self.position == "left" and self.x > self.left_x:
            self.moving = True
            self.x -= self.speed
        elif self.position == "left" and self.x < self.left_x:
            self.x = self.left_x
        elif self.position == "left" and self.x > self.right_x:
            self.x = self.right_x
        else:
            if self.moving and self.row_callback is not None:
                self.row_callback()
            self.moving = False
        self.draw()
