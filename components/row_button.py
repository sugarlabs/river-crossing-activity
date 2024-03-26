import config
import utils
import pygame
from components.common import Clickable, Drawable


class RowButton(Clickable, Drawable):
    def __init__(self, x, y, w=None, h=None):
        super().__init__()

        self.gameDisplay = pygame.display.get_surface()

        image = config.images.get("arrow")
        self.img = utils.scale_image_maintain_ratio(image, w=w, h=h)
        self.set_image_rect(self.img, x, y)
        self.direction = "left"

        self.scale_factor = 0.1

    def flip(self):
        self.img = pygame.transform.flip(self.img, True, False)

    def update(self):
        Drawable.update(self)
        Clickable.update(self)

        if self.hovered():
            self.set_image_rect(self.img, scale=1 + self.scale_factor)
        else:
            self.set_image_rect(self.img, scale=1)
