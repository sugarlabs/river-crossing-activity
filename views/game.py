import pygame
from views import game as gamescreen
import config

def view(game):
    vw = game.vw
    vh = game.vh

    game.set_background(config.images.get("background"))

    land_width = vw(35)
    land_left = config.images.get("land_left")
    m_h = land_width * (land_left.get_height() / land_left.get_width())
    land_left = pygame.transform.scale(land_left, (int(land_width), int(m_h)))

    def draw():
        game.gameDisplay.blit(land_left, (0, int(vh(100) - 0.9 * land_left.get_height())))

    def update():
        draw()

    game.update_function = update
