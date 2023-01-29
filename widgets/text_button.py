from widgets.base_button import BaseButton
from tkinter import Button


class TextButton(BaseButton):
    def __init__(self, root, width, height, text):
        super().__init__(root, width, height)
        self.text = text
        self.widget = Button(self.root,
                             bg=self.button_color,
                             fg=self.text_color,
                             text=self.text,
                             padx=self.padx,
                             pady=self.pady,
                             font=self.font,
                             command=self.command)

    def update(self):
        self.widget = Button(self.root,
                             bg=self.button_color,
                             fg=self.text_color,
                             text=self.text,
                             padx=self.padx,
                             pady=self.pady,
                             font=self.font,
                             command=self.command)

        return self.widget
