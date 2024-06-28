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


import os
import pygame
from font import Font


themes = {}
themes["default"] = (
    {"colors": {"text": (0, 0, 0), "bg": (215, 186, 137)},
    "primary_font": "Wood.ttf",
    "secondary_font": "Geist.ttf"}
)


theme = "default"  # Set initial theme
font_primary = Font()
font_secondary = Font()
colors = {}
images = {}


def set_theme(theme_name):
    global theme
    if theme_name in themes.keys():
        theme = theme_name
        load_assets()


def load_images():
    images = {}
    directory = f"assets/images/{theme}"
    for filename in os.listdir(directory):
        if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
            file_path = os.path.join(directory, filename)
            try:
                image = pygame.image.load(file_path)
                base_filename = os.path.splitext(filename)[0]
                images[base_filename] = image
            except pygame.error as err:
                print(f"Error loading image '{file_path}': {err}")
    return images


def load_assets():
    global colors, images

    images = load_images()

    primary_font_name = themes[theme]["primary_font"]
    font_primary.intialize(f"assets/fonts/{primary_font_name}")

    secondary_font_name = themes[theme]["secondary_font"]
    font_secondary.intialize(f"assets/fonts/{secondary_font_name}")

    colors = themes[theme]["colors"]
