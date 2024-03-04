import os
import pygame

themes = ["default"]
theme = themes[0] # Set initial theme

images = {}

def set_theme(theme):
    if theme in themes:
        theme = theme
        load_assets()

def load_images():
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
    load_images()
