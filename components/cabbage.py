import config, utils, pygame

class Cabbage:
    def __init__(self, x, bottom, w = None, h = None):
        self.gameDisplay = pygame.display.get_surface()

        self.image = utils.scale_image_maintain_ratio(config.images.get("cabbage"), w = w, h = h)

        self.x = x
        self.y = bottom - self.image.get_height()

        self.on_click = None

    def draw(self):
        self.gameDisplay.blit(self.image, (self.x, self.y))

    def update(self):
        self.draw()
