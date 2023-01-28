from tkinter import Button
from constants.button_shape_theme import *
from constants.font_theme import *
from constants.color_theme import *


class BaseButton:
    def __init__(self, root, width, height):
        self.root = root
        self.width = width
        self.height = height

        self.command = lambda: print("No commands")

        self.button_color = button_background
        self.text_color = button_foreground
        self.padx = button_padding_x
        self.pady = button_padding_y
        self.font = button_font

    def set_command(self, command):
        self.command = command
