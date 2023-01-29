import tkinter as tk
from widgets.text_button import TextButton
from widgets.icon_button import IconButton
from widgets.custom_label import CustomLabel

from constants.window_theme import *

from services.stock import *


def center(toplevel):
    toplevel.update_idletasks()

    # Tkinter way to find the screen resolution
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()

    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width / 2 - size[0] / 2
    y = screen_height / 2 - size[1] / 2

    toplevel.geometry("+%d+%d" % (x, y))


# mid frame
current_mid_col = 0
current_mid_row = 0
max_mid_col = 7
max_mid_row = 2

row_weight = 1
col_weight = 10
# column major


def add_to_mid_frame(widget):
    global max_mid_col, max_mid_row, current_mid_col, current_mid_row

    if (current_mid_col == max_mid_col):
        print("max capacity filled for middle frame")
        return

    widget.grid(row=current_mid_row,
                column=current_mid_col, sticky="W", padx=10)

    current_mid_row += 1

    if (current_mid_row == max_mid_row):
        current_mid_col += 1
        current_mid_row = 0

    return


def main():
    root = tk.Tk(className=" " + win_name)

    win_frame = tk.Frame(root, relief='sunken')
    win_frame.pack(fill=tk.BOTH, expand=True)
    root.geometry(win_size)
    root.option_add("*font", font_family)
    center(root)

    ##
    win_frame.columnconfigure(0, weight=1)
    win_frame.rowconfigure(0, weight=15)
    win_frame.rowconfigure(1, weight=1)
    win_frame.rowconfigure(2, weight=2)

    top_frame = tk.Frame(win_frame)
    mid_frame = tk.Frame(win_frame)
    bottom_frame = tk.Frame(win_frame, bg="lightgray")

    top_frame.grid(row=0, column=0, sticky="NESW")
    mid_frame.grid(row=1, column=0, sticky="NESW")
    bottom_frame.grid(row=2, column=0, sticky="NESW")

    for i in range(max_mid_row):
        mid_frame.rowconfigure(i, weight=row_weight)
    for j in range(max_mid_col):
        mid_frame.columnconfigure(j, weight=col_weight)

    ##

    ##
    stock_name = "MSFT"
    # stock_res = get_stock(stock_name)
    # times_data, prices_data = get_time_price(stock_res)
    specs = ["Open", "Close", "High", "Low", "Volume", "Market Cap", "52 Week High",
             "52 Week Low", "Dividend Yield", "P/E Ratio", "P/B Ratio", "PEG Ratio"]

    profits = ["Cash Available", "Total Gain"]
    profit_frame = tk.Frame(
        mid_frame, highlightbackground="lightgray", highlightthickness=2, )
    profit_frame.columnconfigure(0, weight=1)
    profit_frame.rowconfigure(0, weight=1)
    profit_frame.rowconfigure(1, weight=1)
    for spec in specs:
        label = CustomLabel(mid_frame, text=spec + ":")
        add_to_mid_frame(label.widget)

    cash_avail = CustomLabel(profit_frame, text=profits[0] + ": $")
    total_gain = CustomLabel(profit_frame, text=profits[1] + ": $")
    cash_avail.widget.grid(row=0, column=0, sticky="W", padx=10)
    total_gain.widget.grid(row=1, column=0, sticky="W", padx=10)

    profit_frame.grid(row=0, column=(max_mid_col - 1),
                      sticky="NSWE", rowspan=2)


# ##
    root.mainloop()


if __name__ == '__main__':
    main()
