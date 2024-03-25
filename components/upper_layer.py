import config, pygame, random, utils
from components.common import Drawable

class Upper_Layer(Drawable):
    def __init__(self):
        super().__init__()

        self.gameDisplay = pygame.display.get_surface()

        self.direction = "right" #direction of clouds (wind)
        self.h = 124
        self.w = 1240
        self.images = []
        for i in config.images.keys():
            if i.startswith("upper-layer"):
                self.images.append(config.images.get(i).copy())
        self.floaters = []

    def generate(self, w, speed):
        image = random.choice(self.images)
        image = utils.scale_image_maintain_ratio(image, w = w)
        x = 0 - w if self.direction == "right" else self.w + w
        y = random.random() * (self.h - image.get_height())
        floater = {"x" : x, "y" : y, "image" : image.copy(), "speed" : speed}
        self.floaters.append(floater)

    def update(self):
        Drawable.update(self)

        image = pygame.Surface((self.w, self.h), pygame.SRCALPHA, 32).convert_alpha()
        for floater in self.floaters:
            floater["x"] += floater["speed"] * (1 if self.direction == "right" else -1)
            image.blit(floater["image"], (floater["x"], floater["y"]))
            
            if self.direction == "right" and floater["x"] > self.w * 1.5:
                del floater
            if self.direction == "left" and floater["x"] < - self.w * 1.5:
                del floater
        
        self.set_image_rect(image)