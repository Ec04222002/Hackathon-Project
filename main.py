import tkinter as tk
from widgets.text_button import TextButton
from widgets.icon_button import IconButton
from widgets.custom_label import CustomLabel

from constants.window_theme import *


def center(toplevel):
    toplevel.update_idletasks()

    # Tkinter way to find the screen resolution
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()

    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width / 2 - size[0] / 2
    y = screen_height / 2 - size[1] / 2

    toplevel.geometry("+%d+%d" % (x, y))


def main():
    root = tk.Tk(className=win_name)
    root.geometry(win_size)
    center(root)

    submit_btn = TextButton(root=root, width=100, height=50, text="Submit")

    submit_btn.widget.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
