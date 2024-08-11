# Copyright (C) 2024 Spandan Barve
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from components.button import Button
from components.cabbage import Cabbage
import views.menu as menu
import config
import pygame

themes = ["default", "3d"]
theme_names = ["Classic", "Classic 3D"]

def view(game):
    buttons = []
    vw = game.vw
    vh = game.vh

    game.set_background(None)

    theme_icon = Cabbage(vw(50) - 200, vh(18), w = 200)

    theme_text = config.font_secondary.xxl.render(theme_names[themes.index(config.theme)], True, config.colors["text"])
    theme_text_rect = theme_text.get_rect()
    
    themes_button = Button(vw(50), vh(28), "Change Theme", h=vh(15),
                         font=config.font_primary.lg)
    def change_theme():
        config.set_theme(themes[(themes.index(config.theme) + 1) % len(themes)])
        game.set_screen(view)
    themes_button.on_click = lambda: change_theme()
    buttons.append(themes_button)
    
    back_button = Button(vw(50), vh(75), "Done", h=vh(15),
                         font=config.font_primary.lg)
    back_button.on_click = lambda: game.set_screen(menu.view)
    buttons.append(back_button)

    def update():
        game.gameDisplay.blit(theme_text, pygame.Rect(vw(50) - 32, vh(10), theme_text_rect.width, theme_text_rect.height))
        for btn in buttons:
            btn.update()
        theme_icon.update()

    game.update_function = update
