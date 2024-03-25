import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pygame

from sugar3.activity.activity import Activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.activity.widgets import StopButton

import sugargame.canvas

from gettext import gettext as _
from main import RiverCrossing


class RiverCrossingActivity(Activity):

    def __init__(self, handle):
        Activity.__init__(self, handle)
        self.max_participants = 1
        self.sound = True
        self.game = RiverCrossing()
        self.build_toolbar()
        self.game.canvas = sugargame.canvas.PygameCanvas(
                self,
                main=self.game.run,
                modules=[pygame.display, pygame.font, pygame.mixer])
        self.set_canvas(self.game.canvas)
        self.game.canvas.grab_focus()

    def build_toolbar(self):
        toolbar_box = ToolbarBox()
        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)
        activity_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(False)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        help_button = ToolButton('toolbar-help')
        help_button.set_tooltip(_('How To Play'))
        help_button.connect('clicked', self.show_help)
        toolbar_box.toolbar.insert(help_button, -1)
        help_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()
        stop_button.connect('clicked', self._stop_cb)

    def show_help(self, button):
        self.game.show_help()

    def _stop_cb(self, button):
        self.game.running = False