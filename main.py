import tkinter as tk
from widgets.text_button import TextButton
from widgets.icon_button import IconButton
from widgets.custom_label import CustomLabel
# from widgets.ticker_graph import TickerGraph
from constants.window_theme import *
import widgets.ticker_graph as graph
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

    global top_frame
    root = tk.Tk(className=" " + win_name)

    root.geometry(win_size)
    root.option_add("*font", font_family)
    center(root)

    ##
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=7)
    root.rowconfigure(1, weight=2)
    root.rowconfigure(2, weight=2)

    top_frame = tk.Frame(root)
    mid_frame = tk.Frame(root)
    bottom_frame = tk.Frame(root, bg="lightgray")

    top_frame.grid(row=0, column=0, sticky="NESW")
    mid_frame.grid(row=1, column=0, sticky="NESW")
    bottom_frame.grid(row=2, column=0, sticky="NESW")

    top_frame.columnconfigure(0, weight=4)
    top_frame.columnconfigure(1, weight=1)
    for i in range(max_mid_row):
        mid_frame.rowconfigure(i, weight=row_weight)
    for j in range(max_mid_col):
        mid_frame.columnconfigure(j, weight=col_weight)
    for k in range(4):
        top_frame.rowconfigure(k, weight=1)

    for l in range(3):
        bottom_frame.columnconfigure(i, weight=1)
        bottom_frame.rowconfigure(i, weight=1)

    # print(open_prices_data)
    # creating graphs and start top frame
    ticker = tk.Entry(top_frame, fg="lightgray")
    ticker.insert(0, 'Ticker')

    def delText0(event=None):
        ticker.delete(0, tk.END)
    ticker.bind('<Button>', delText0)
    ticker.grid(row=0, column=1, rowspan=3, sticky="W", padx=7)

    budget = tk.Entry(top_frame, fg="lightgray")
    budget.insert(0, '$ Budget Amount')

    def delText1(event=None):
        budget.delete(0, tk.END)
    budget.bind('<Button>', delText1)
    budget.grid(row=1, column=1, rowspan=2, sticky="W", padx=7)

    options_frame = tk.Frame(top_frame)
    options_frame.columnconfigure(0, weight=1)
    options_frame.columnconfigure(1, weight=1)
    options_frame.columnconfigure(2, weight=1)
    options_frame.columnconfigure(3, weight=1)
    options_frame.rowconfigure(0, weight=1)

    training = tk.Label(options_frame, text='Duration:')
    training.grid(row=0, column=0)
    time = tk.IntVar()
    Option1 = tk.Radiobutton(options_frame, text='5m', variable=time, value=5)
    Option1.grid(row=0, column=1)
    Option2 = tk.Radiobutton(options_frame, text='10m',
                             variable=time, value=10)
    Option2.grid(row=0, column=2)
    Option3 = tk.Radiobutton(options_frame, text='15m',
                             variable=time, value=15)
    Option3.grid(row=0, column=3)

    options_frame.grid(column=1, row=2, sticky="W", padx=5)

    start_reset_frame = tk.Frame(top_frame)
    start_reset_frame.columnconfigure(0, weight=1)
    start_reset_frame.columnconfigure(1, weight=1)
    Start = TextButton(root=start_reset_frame,
                       text="Run ➤", width=110, height=50)
    reset = TextButton(root=start_reset_frame,
                       text="Reset ⟳", width=110, height=50)

    Start.set_command(lambda: handle_run(ticker.get()))
    reset.set_command(handle_reset)
    Start.widget.grid(row=0, column=0, padx=7)
    reset.widget.grid(row=0, column=1, padx=7)
    start_reset_frame.grid(column=1, row=3, sticky="NW")

    # creating specs middle frame

    specs = ["Open", "Close", "High", "Low", "Volume", "Market Cap", "52 Week High",
             "52 Week Low", "Dividend Yield", "P/E Ratio", "P/B Ratio", "PEG Ratio"]

    profits = ["Cash Available", "Total Gain"]

    for spec in specs:
        label = CustomLabel(mid_frame, text=spec + ":")
        add_to_mid_frame(label.widget)
    for profit in profits:
        label = CustomLabel(mid_frame, text=profit + ": $")
        add_to_mid_frame(label.widget)

    graph.draw(top_frame)
    # --------------------------
# Bottom Frame
    control_frame = tk.Frame(bottom_frame, bg="lightgray")
    control_frame.columnconfigure(0, weight=1)
    control_frame.columnconfigure(1, weight=1)
    control_frame.columnconfigure(2, weight=1)
    buy_btn = TextButton(root=control_frame, text="Buy", width=110, height=50)
    sell_btn = TextButton(root=control_frame,
                          text="Sell", width=110, height=50)
    Order_Quantity = tk.Entry(control_frame, fg="lightgray")
    Order_Quantity.insert(0, '$ Amount')

    def delText2(event=None):
        Order_Quantity.delete(0, tk.END)
    Order_Quantity.bind('<Button>', delText2)
    buy_btn.widget.grid(column=2, row=0, padx=8)
    sell_btn.widget.grid(column=1, row=0, padx=8)
    Order_Quantity.grid(column=0, row=0, padx=8)

    control_frame.grid(column=1, row=1)

# ##
    root.mainloop()


def handle_run(symbol):
    stock_res = get_stock(symbol)
    times_data = get_time(stock_res)
    open_prices_data = get_prices(stock_res)['open']

    xlim = (min(times_data), max(times_data))
    ylim = (min(open_prices_data), max(open_prices_data))

    graph.set_data(x=times_data, y=open_prices_data)
    graph.draw(root=top_frame, xlim=xlim, ylim=ylim)


def handle_reset():
    pass


def handle_buy():
    pass


def handle_sell():
    pass


if __name__ == '__main__':
    main()
