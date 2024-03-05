import pygame
import config
import utils

class Boat:
    def __init__(self, left_x, right_x, bottom, w):
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

    def draw(self):
        farmer_x = self.x + self.boat_w * 0.1
        farmer_y = self.y - self.farmer_h * 0.6
        self.gameDisplay.blit(self.farmer, (int(farmer_x), int(farmer_y)))
        
        self.gameDisplay.blit(self.boat, (self.x, self.y))

    def update(self):
        self.draw()
