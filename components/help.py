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
from components.container_box import ContainerBox


class Help():
    def __init__(self, game, w=None, h=None):
        super().__init__()

        self.prev_update_func = None
        self.container = None
        self.clicked = False
        self.prev_bg = None
        self.hidden = True
        self.game = game

    def initialize(self):
        self.container = ContainerBox(self.game.vw(50), self.game.vh(50))

        vw = self.game.vw
        vh = self.game.vh

        self.container.padding_x = 32
        self.container.padding_y = 20

        self.container.gap_x = 5
        self.container.gap_y = 30

        cabbage = config.images.get("cabbage")
        cabbage = utils.scale_image_maintain_ratio(cabbage, h=vh(10))

        wolf = config.images.get("wolf")
        wolf = utils.scale_image_maintain_ratio(wolf, h=vh(10))

        goat = config.images.get("goat")
        goat = utils.scale_image_maintain_ratio(goat, h=vh(10))

        arrow = config.images.get("arrow")
        arrow = utils.scale_image_maintain_ratio(arrow, h=vh(6))

        text_color = config.colors["text"]

        def text(str):
            return config.font_secondary.xl.render(str, True, text_color)

        self.container.add_row()
        self.container.add_element(1, text("Get all"))
        self.container.add_element(1, goat)
        self.container.add_element(1, wolf)
        self.container.add_element(1, cabbage)
        self.container.add_element(1, text("to the right"))

        self.container.add_row()
        self.container.add_element(2, text("Don't leave"))
        self.container.add_element(2, cabbage)
        self.container.add_element(2, text("alone with"))
        self.container.add_element(2, goat)

        self.container.add_row()
        self.container.add_element(3, text("Don't leave"))
        self.container.add_element(3, goat)
        self.container.add_element(3, text("alone with"))
        self.container.add_element(3, wolf)

        self.container.add_row()
        self.container.add_element(4, text("Click on your boat to unmount it"))

        self.container.add_row()
        self.container.add_element(5, text("Click"))
        self.container.add_element(5, arrow)
        self.container.add_element(5, text("to row your boat"))

        self.container.add_row()
        self.container.add_row()
        self.container.add_element(7, text("< Click to continue >"))

    def show(self):
        self.prev_bg = self.game.bg
        bg = self.game.gameDisplay.copy()
        bg.fill((120, 120, 120), special_flags=pygame.BLEND_MULT)
        self.game.set_background(bg)
        self.prev_update_func = self.game.update_function
        self.game.update_function = self.update
        self.hidden = False

    def hide(self):
        self.game.update_function = self.prev_update_func
        self.game.set_background(self.prev_bg)
        self.hidden = True

    def update(self):
        if self.container is not None and not self.hidden:
            self.container.update()

        pressed_btn = pygame.mouse.get_pressed()[0]

        if self.clicked and pressed_btn != 1:
            self.hide()

        if pressed_btn == 1:
            self.clicked = True
