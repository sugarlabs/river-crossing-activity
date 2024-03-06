from components.button import Button
from views import game as gamescreen
import config

def view(game):
    buttons = []
    vw = game.vw
    vh = game.vh

    buttons.append(Button(vw(50), vh(50), "Play", h = vh(20), font = config.font_primary.xl))

    def update():
        for btn in buttons:
            btn.update()

    game.update_function = update
