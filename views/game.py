import pygame
from views import game as gamescreen
import config
from components.boat import Boat

def view(game):
    vw = game.vw
    vh = game.vh

    game.set_background(config.images.get("background"))

    land_width = vw(30)
    land_left = config.images.get("land_left")
    land_right = config.images.get("land_right")

    m_h = land_width * (land_left.get_height() / land_left.get_width())
    land_left = pygame.transform.scale(land_left, (int(land_width), int(m_h)))

    m_h = land_width * (land_right.get_height() / land_right.get_width())
    land_right = pygame.transform.scale(land_right, (int(land_width), int(m_h)))

    boat_padding = vw(2)
    boat = Boat(land_width + boat_padding, vw(100) - land_width - boat_padding, vh(90), vw(18))

    def draw():
        game.gameDisplay.blit(land_left, (0, int(vh(100) - 0.9 * land_left.get_height())))
        game.gameDisplay.blit(land_right, (int(vw(100) - land_width), int(vh(100) - 0.9 * land_right.get_height())))

    def update():
        boat.update()
        draw()

    game.update_function = update
