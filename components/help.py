import config, utils, pygame
from components.common import Clickable, Drawable
from components.container_box import ContainerBox

class Help():
    def __init__(self, game, w = None, h = None):
        super().__init__()

        self.prev_update_func = None
        self.container = None
        self.hidden = True
        self.game = game

    def initialize(self):
        self.container = ContainerBox(self.game.vw(50), self.game.vh(50))

        vw = self.game.vw
        vh = self.game.vh

        self.container.padding_x = 32
        self.container.padding_y = 20

        self.container.gap_x = 10
        self.container.gap_y = 20

        cabbage = config.images.get("cabbage")
        cabbage = utils.scale_image_maintain_ratio(cabbage, h = vh(10))

        wolf = config.images.get("wolf")
        wolf = utils.scale_image_maintain_ratio(wolf, h = vh(10))
        
        goat = config.images.get("goat")
        goat = utils.scale_image_maintain_ratio(goat, h = vh(10))

        arrow = config.images.get("arrow")
        arrow = utils.scale_image_maintain_ratio(arrow, h = vh(6))

        text_color = config.colors["text"]
        def text(str):
            return config.font_secondary.xl.render(str, True, text_color)

        self.container.add_row()
        self.container.add_element(1, text("Don't leave"))
        self.container.add_element(1, cabbage)
        self.container.add_element(1, text("alone with"))
        self.container.add_element(1, goat)
        
        self.container.add_row()
        self.container.add_element(2, text("Don't leave"))
        self.container.add_element(2, goat)
        self.container.add_element(2, text("alone with"))
        self.container.add_element(2, wolf)

        self.container.add_row()
        self.container.add_element(3, text("Click"))
        self.container.add_element(3, arrow)
        self.container.add_element(3, text("to row your boat"))
        

    def show(self):
        bg = self.game.gameDisplay.copy()
        bg.fill((120, 120, 120), special_flags = pygame.BLEND_MULT)
        self.game.set_background(bg)
        self.prev_update_func = self.game.update_function
        self.game.update_function = None
        
        self.hidden = False

    def hide(self):
        self.hidden = True

    def update(self):
        if self.container is not None and not self.hidden:
            self.container.update()
