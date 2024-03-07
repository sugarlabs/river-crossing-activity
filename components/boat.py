import pygame
import config
import utils
from components.common import Clickable

class Boat(Clickable):
    def __init__(self, left_x, right_x, bottom, w):
        super().__init__()

        self.gameDisplay = pygame.display.get_surface()

        boat = config.images.get("boat")
        farmer = config.images.get("farmer")

        self.boat = utils.scale_image_maintain_ratio(boat, w = w)
        self.farmer = utils.scale_image_maintain_ratio(farmer, w = w // 3)

        self.boat_w = self.boat.get_width()
        self.boat_h = self.boat.get_height()

        self.farmer_h = self.farmer.get_height()
        
        self.left_x = left_x
        self.right_x = right_x
        self.x = self.left_x
        self.y = bottom - self.boat_h // 2

        self.holding = None
        self.holding_w = None
        self.holding_h = None

        self.position = "left"
        self.moving = False
        self.row_callback = None

    def hold(self, image):
        if image is None:
            self.holding = None
            return
        self.holding = utils.scale_image_maintain_ratio(image, h = self.farmer_h // 2)
        self.holding_w, self.holding_h = self.holding.get_size()


    def draw(self):
        farmer_x = self.x + self.boat_w * 0.1
        farmer_y = self.y - self.farmer_h * 0.6
        self.gameDisplay.blit(self.farmer, (int(farmer_x), int(farmer_y)))

        if self.holding is not None:
            holding_x = self.x + self.boat_w * 0.9 - self.holding_w
            holding_y = self.y - self.holding_h * 0.5
            self.gameDisplay.blit(self.holding, (int(holding_x), int(holding_y)))

        self.gameDisplay.blit(self.boat, (self.x, self.y))

    def row(self, callback = None):
        if self.moving:
            return

        if self.position == "left":
            self.position = "right"
        elif self.position == "right":
            self.position = "left"

        self.row_callback = callback

    def update(self):
        Clickable.update(self)
        self.rect = self.boat.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.draw()

        if self.position == "right" and self.x <= self.right_x:
            self.moving = True
            self.x += 3
        elif self.position == "left" and self.x >= self.left_x:
            self.moving = True
            self.x -= 3
        else:
            if self.moving and self.row_callback is not None:
                self.row_callback()
            self.moving = False
