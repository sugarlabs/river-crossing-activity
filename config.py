import os
import pygame
from font import Font

themes = {}

def define_theme(name, text_color, bg_color, font_name):
    themes[name] = ({
                   "colors" : {"text" : text_color, "bg" : bg_color},
                   "font" : font_name
                   })

define_theme("default", (0, 0, 0), (0, 100, 50), "Geist.ttf")

theme = "default" # Set initial theme
font = Font()
colors = {}
images = {}

def set_theme(theme_name):
    global theme
    if theme_name in themes.keys():
        theme = theme_name
        load_assets()

def load_images():
    images = {}
    directory = f"assets/images/themes/{theme}"
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

    font_name = themes[theme]["font"]
    font.intialize(f"assets/fonts/{font_name}")

    colors = themes[theme]["colors"]
