from widgets.base_button import BaseButton
from tkinter import Button


from tkinter import LEFT, RIGHT

class IconButton(BaseButton):
    def __init__(self, width, height, icon, text):
        super().__init__()
        self.icon = icon
        self.is_icon_left = True
        self.text = text
        self.widget = self.update()

    def update(self):
        self.widget = Button(self.root,
                             bg=self.button_color,
                             fg=self.text_color,
                             text=self.text,
                             padx=self.padx,
                             pady=self.pady,
                             font=self.font,
                             image= self.icon,
                             compound= LEFT if self.is_icon_left else RIGHT,
                             command=self.command)

        return self.widget