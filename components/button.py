import pygame
import config
import utils
from components.common import Clickable, Drawable


class Button(Clickable, Drawable):
    def __init__(self, x, y,
                 label, w=None, h=None,
                 scale_factor=0.05, font=None):
        super().__init__()

        self.gameDisplay = pygame.display.get_surface()

        button_image = config.images.get("button")
        self.img = utils.scale_image_maintain_ratio(button_image, w=w, h=h)
        btn_rect = self.img.get_rect()

        if font is None:
            font = config.font_primary.md

        # Generate and blit the Label on button
        text_color = config.colors["text"]
        label = font.render(label, True, text_color)
        label_rect = label.get_rect()
        label_rect.x = btn_rect.width // 2 - label_rect.width // 2
        label_rect.y = btn_rect.height // 2 - int(label_rect.height * 0.7)
        self.img.blit(label, label_rect)

        self.set_image_rect(self.img,
                            x - self.img.get_width() // 2,
                            y - self.img.get_height() // 2)
        self.scale_factor = scale_factor

    def update(self):
        Clickable.update(self)
        Drawable.update(self)

        if self.hovered():
            self.set_image_rect(self.img, scale=1 + self.scale_factor)
        else:
            self.set_image_rect(self.img, scale=1)
