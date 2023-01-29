from tkinter import Label
from constants.button_theme import *
from constants.label_theme import *


class CustomLabel:
    def __init__(self, root, text):
        self.text = text
        self.root = root
        self.text_color = label_foreground
        # self.background_color = label_background
        self.font = label_font
        self.widget = Label(
            root, font=label_font, text=text,  fg=label_foreground)

    def update(self):
        self.widget = Label(
            self.root, font=self.font, text=self.text,  fg=label_foreground)

        return self.widget
