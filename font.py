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


class Font:
    def __init__(self):
        self.sm = None
        self.md = None
        self.lg = None
        self.xl = None
        self.xxl = None

    def intialize(self, file):
        self.sm = self.load_font(file, 10)
        self.md = self.load_font(file, 16)
        self.lg = self.load_font(file, 20)
        self.xl = self.load_font(file, 26)
        self.xxl = self.load_font(file, 36)

    def load_font(self, file, size):
        return pygame.font.Font(file, size)
