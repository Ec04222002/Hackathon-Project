import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.animation import FuncAnimation
import datetime as dt
import matplotlib.dates as mdates


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
        self.animation_disp = 0.1
        self.animation_frame_time = 200

    def animate_frame(self, i):

        print(i)
        self.x_plot_data.append(self.x_time_data[int(i)])
        self.y_plot_data.append(self.y_open_price_data[int(i)])

        self.line.set_xdata(self.x_plot_data)
        self.line.set_ydata(self.y_plot_data)
        return self.line

    def make_graph(self):
        dates = self.x_time_data
        self.x_time_data = [dt.datetime.strptime(
            d, '%m/%d/%Y').date() for d in dates]
        x = self.x_time_data
        y = self.y_open_price_data

        self.ax.set_xlim(x[0], x[-1])
        self.ax.set_ylim(y[0], y[-1])
        self.line, = self.ax.plot(0, 0)

        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        plt.gcf().autofmt_xdate()

    def animate(self):
        print(self.end_interval)
        animation = FuncAnimation(
            self.fig, func=self.animate_frame, frames=np.arange(self.start_interval, self.end_interval, self.animation_disp), interval=self.animation_frame_time)

        plt.show()
        # return


a = TickerGraph(x_axis_name="Open Price", y_axis_name="Time", x_time_data=[
                "01/02/1991", "01/03/1991", "01/04/1991"], y_open_price_data=[1, 2, 3])

a.make_graph()
a.animate()
