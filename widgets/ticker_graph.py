import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib import pyplot as plt, animation
import numpy as np

import datetime as dt


class TickerGraph:

    def __init__(self, x_axis_name, y_axis_name, x_time_data, y_open_price_data):
        self.x_axis_name = x_axis_name
        self.y_axis_name = y_axis_name
        self.x_time_data = x_time_data
        self.y_open_price_data = y_open_price_data
        self.x_plot_data = []
        self.y_plot_data = []
        self.fig, self.ax = plt.subplots()

        self.line = None

        self.start_interval = 0
        self.end_interval = len(y_open_price_data)
        self.animation_disp = 0.2
        self.animation_frame_time = 100

        plt.rcParams["figure.figsize"] = [7.00, 3.50]

        plt.rcParams["figure.autolayout"] = True

   def animate_frame(self, i):

        print(self.x_time_data[int(i)])
        print(self.y_open_price_data[int(i)])
        self.x_plot_data.append(self.x_time_data[int(i)])
        self.y_plot_data.append(self.y_open_price_data[int(i)])

        self.line.set_xdata(self.x_plot_data)
        self.line.set_ydata(self.y_plot_data)
        return self.line

    def make_graph(self):
        dates = self.x_time_data

        self.x_time_data = [dt.datetime.strptime(
            d, "%Y-%m-%d %H:%M:%S") for d in dates]

        x = self.x_time_data
        y = self.y_open_price_data

        self.ax.set_xlim(0, 1000)
        self.ax.set_ylim(100, 1000)
        self.line, = self.ax.plot(0, 0)

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
        plt.grid()

    def init_animate(self):
        self.line.set_data([], [])
        return self.line

    def animate(self):
        # print(self.end_interval)
        animation = FuncAnimation(
            self.fig, func=self.animate_frame, init_func=self.init_animate, frames=np.arange(self.start_interval, self.end_interval, self.animation_disp), interval=self.animation_frame_time)
        print()
        plt.show()
        # return


# a = TickerGraph(x_axis_name="Open Price", y_axis_name="Time", x_time_data=[
#                 "2018-06-29 08:15:27", "2018-06-29 08:25:27", "2018-06-29 08:25:27"], y_open_price_data=[1, 2, 3])

# a.make_graph()
# a.animate()
