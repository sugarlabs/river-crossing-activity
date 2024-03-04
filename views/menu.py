from components.button import Button

def view(game):
    buttons = []
    vw = game.vw
    vh = game.vh

    buttons.append(Button(vw(50), vh(20), "Play", lambda x=32 : print(f"ok {x}"), h = vh(10)))

    def update():
        for btn in buttons:
            btn.update()

    game.update_function = update
