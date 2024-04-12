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
import pygame


class ContainerBox():
    def __init__(self, x, y):
        self.gameDisplay = pygame.display.get_surface()

        self.rows = []
        self.image = None
        self.gap_y, self.gap_x = 0, 0
        self.padding_x, self.padding_y = 0, 0

        self.w, self.h = 0, 0
        self.x, self.y = 0, 0

        self.i_x, self.i_y = x, y

        self.bg = config.colors["bg"]

    def add_row(self):
        self.rows.append({"elements": [], "height": 0, "width": 0})
        self.update_layout()
        return len(self.rows) - 1

    def define_row(self, row, elements):  # Elements of pygame.Surface type array
        for element in elements:
            self.rows[row - 1]["elements"].append(element.copy())
            self.update_layout()

    def add_element(self, row, element):  # Element of pygame.Surface type
        self.rows[row - 1]["elements"].append(element.copy())
        self.update_layout()

    def update_layout(self):
        self.w, self.h = 0, 0
        w_max = 0
        for row in self.rows:
            row["width"] = 0
            row["height"] = 0
            for i, element in enumerate(row["elements"]):
                e_w, e_h = element.get_size()
                row["width"] += e_w + (self.gap_x)
                if e_h > row["height"]:
                    row["height"] = e_h
            if row["width"] > w_max:
                w_max = row["width"]

            self.h += row["height"]

        self.w = w_max + 2 * self.padding_x
        self.h += 2 * self.padding_y + (len(self.rows) - 1) * (self.gap_y)

        self.x = int(self.i_x - self.w / 2)
        self.y = int(self.i_y - self.h / 2)

        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(self.bg)
        y = self.padding_y
        for row in self.rows:
            row_surf = pygame.Surface((row["width"], row["height"]))
            row_surf.fill(config.colors["bg"])
            row_center = row["height"] / 2
            x = 0
            for e in row["elements"]:
                row_surf.blit(e, (x, row_center - e.get_height() / 2))
                x += e.get_width() + self.gap_x
            x = self.w / 2 - row["width"] / 2
            self.image.blit(row_surf, (x, y))
            y += row["height"] + self.gap_y

    def update(self):
        self.gameDisplay.blit(self.image, (self.x, self.y))
