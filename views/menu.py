from components.button import Button
from views import game as gamescreen
import config

def view(game):
    buttons = []
    vw = game.vw
    vh = game.vh

    play_button = Button(vw(50), vh(50), "Play", h = vh(20), font = config.font_primary.xl)
    play_button.on_click = lambda : game.set_screen(gamescreen.view)
    buttons.append(play_button)

    def update():
        for btn in buttons:
            btn.update()

    game.update_function = update
