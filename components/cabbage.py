import config
import utils
import pygame
from components.common import Clickable, Drawable


class Cabbage(Clickable, Drawable):
    def __init__(self, x, bottom, w=None, h=None):
        super().__init__()

        self.gameDisplay = pygame.display.get_surface()

        image = utils.scale_image_maintain_ratio(config.images.get("cabbage"),
                                                 w=w, h=h)
        self.set_image_rect(image, x, bottom - image.get_height())

    def update(self):
        Clickable.update(self)
        Drawable.update(self)
