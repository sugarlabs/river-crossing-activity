import pygame
import config
from components.boat import Boat
from components.goat import Goat
from components.wolf import Wolf
from components.cabbage import Cabbage

def view(game):
    vw = game.vw
    vh = game.vh

    game.set_background(config.images.get("background"))

    land_width = vw(30)
    land_left = config.images.get("land_left")
    land_right = config.images.get("land_right")

    land_left_h = land_width * (land_left.get_height() / land_left.get_width())
    land_left = pygame.transform.scale(land_left, (int(land_width), int(land_left_h)))

    land_right_h = land_width * (land_right.get_height() / land_right.get_width())
    land_right = pygame.transform.scale(land_right, (int(land_width), int(land_right_h)))

    boat_padding = vw(2)
    boat = Boat(land_width + boat_padding, vw(100) - land_width - boat_padding, vh(90), vw(18))
    
    objects_count = 3
    land_object_width = vw(9)
    objects_left = []
    object_in_boat = None
    objects_right = []

    def define_objects(left, right):
        #Left Land
        gap = (land_width - objects_count * land_object_width) / (objects_count + 1)
        bottom = vh(100) - land_left_h // 4
        for i, Obj in enumerate(left):
            obj = Obj(gap * (i + 1) + land_object_width * i, bottom, w = land_object_width)
            objects_left.append(obj)
        
        #Right Land
        gap = (land_width - objects_count * land_object_width) / (objects_count + 1)
        bottom = vh(100) - land_right_h // 4
        for i, Obj in enumerate(right):
            obj = Obj(vw(100) - (gap * (i + 1) + land_object_width * (i + 1)), bottom, w = land_object_width)
            objects_right.append(obj)

    define_objects([Goat, Cabbage], [Wolf])

    def draw():
        game.gameDisplay.blit(land_left, (0, int(vh(100) - 0.9 * land_left.get_height())))
        game.gameDisplay.blit(land_right, (int(vw(100) - land_width), int(vh(100) - 0.9 * land_right.get_height())))

        for obj in objects_left:
            obj.update()
        for obj in objects_right:
            obj.update()

    def update():
        boat.update()
        draw()

    game.update_function = update
