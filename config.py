import os
import pygame
from font import Font


themes = {}


def define_theme(name, text_color, bg_color,
                 primary_font_name, scondary_font_name):

    themes[name] = ({"colors": {"text": text_color, "bg": bg_color},
                     "primary_font": primary_font_name,
                     "secondary_font": scondary_font_name
                     })


define_theme("default", (0, 0, 0), (215, 186, 137), "Wood.ttf", "Geist.ttf")


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
