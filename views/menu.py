from components.button import Button
from views import game as gamescreen
import config
import utils
import math


def view(game):
    buttons = []
    vw = game.vw
    vh = game.vh

    game.set_background(config.images.get("menu_bg"))

    play_button = Button(vw(50), vh(55), "Play", h=vh(20), font=config.font_primary.xl)
    play_button.on_click = lambda: game.set_screen(gamescreen.view)
    buttons.append(play_button)

    play_button = Button(vw(50), vh(78),
                         "Settings", h=vh(20),
                         font=config.font_primary.xl)
    # TODO - make settings screen view (include theme and speed option)
    # Connect view with this button
    play_button.on_click = lambda: print("Coming Soon")
    buttons.append(play_button)

    title_h = vh(25)
    title = config.images.get("logo")
    title = utils.scale_image_maintain_ratio(title, h=title_h)

    step = {"ticks": 0}

    def draw():
        title_angle = math.sin(step["ticks"] / 30) * 10
        title_scale = math.sin(45 + step["ticks"] / 40) * 0.1
        logo = utils.scale_image_maintain_ratio(title,
                                                h=title_h * (1 + title_scale))
        logo, rect = utils.rotate_by_center(logo,
                                            title_angle,
                                            vw(50),
                                            vh(22.5))
        game.gameDisplay.blit(logo, rect)

    def update():
        step["ticks"] += 1

        # Cap ticks to avoid big numbers for calculation
        if step["ticks"] > 10e2:
            step["ticks"] = 0

        draw()
        for btn in buttons:
            btn.update()

    game.update_function = update
