import pygame
import config
from components.boat import Boat
from components.goat import Goat
from components.wolf import Wolf
from components.cabbage import Cabbage
from components.row_button import RowButton

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
    boat_width = vw(18)
    boat = Boat(land_width + boat_padding, vw(100) - land_width - boat_width - boat_padding, vh(90), boat_width)

    row_button_width = vw(8)
    row_button = RowButton(vw(50) - row_button_width // 2, vh(40), w= row_button_width)
    row_button.on_click = lambda: boat.row(callback= lambda : row_button.flip())

    objects_count = 3
    land_object_width = vw(9)
    objects_left = []
    object_in_boat = {"class": None}
    objects_right = []

    def boat_click_action():
        if boat.moving:
            return
        
        boat.hold(None)
        left = list(map(type, objects_left))
        right = list(map(type, objects_right))
        if boat.position == "left":
            left.append(object_in_boat["class"])
            define_objects(left = left)
        if boat.position == "right":
            right.append(object_in_boat["class"])
            define_objects(right = right)

        object_in_boat["class"] = None            
    
    def get_land_object_click_function(land_arr, obj, condition_func):
        def func():
            if boat.moving or not condition_func():
                return
            
            if boat.holding is not None and object_in_boat["class"] is not None:
                return
            
            index = land_arr.index(obj)
            object_in_boat["class"] = type(land_arr[index])
            boat.hold( land_arr[index].image)
            del land_arr[index]

        return func

    def define_objects(left = None, right = None):
        #Left Land
        if left is not None:
            objects_left.clear()
            gap = (land_width - objects_count * land_object_width) / (objects_count + 1)
            bottom = vh(100) - land_left_h // 4
            for i, Obj in enumerate(left):
                obj = Obj(gap * (i + 1) + land_object_width * i, bottom, w = land_object_width)
                obj.on_click = get_land_object_click_function(objects_left, obj, lambda : boat.position == "left")
                objects_left.append(obj)
        
        #Right Land
        if right is not None:
            objects_right.clear()
            gap = (land_width - objects_count * land_object_width) / (objects_count + 1)
            bottom = vh(100) - land_right_h // 4
            for i, Obj in enumerate(right):
                obj = Obj(vw(100) - (gap * (i + 1) + land_object_width * (i + 1)), bottom, w = land_object_width)
                obj.on_click = get_land_object_click_function(objects_right, obj, lambda : boat.position == "right")
                objects_right.append(obj)

    define_objects([Goat, Cabbage, Wolf], [])
    boat.on_click = boat_click_action

    def draw():
        game.gameDisplay.blit(land_left, (0, int(vh(100) - 0.9 * land_left.get_height())))
        game.gameDisplay.blit(land_right, (int(vw(100) - land_width), int(vh(100) - 0.9 * land_right.get_height())))

    def update():
        draw()
        boat.update()
        row_button.update()

        for obj in objects_left:
            obj.update()
        for obj in objects_right:
            obj.update()

    game.update_function = update
