
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib import pyplot as plt, animation, figure, ticker
import numpy as np

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True


x_data = None
y_data = None


def set_data(x=None, y=None):
    global x_data, y_data
    x_data = x
    y_data = y

    print(x_data, y_data)
    return


def draw(root, xlim=(0, 2), ylim=(-2, 2), frames=200, interval=20):
    global fig, line, ax
    plt.axes(xlim=xlim, ylim=ylim)
    fig = plt.Figure(dpi=100)

    isDefault = x_data == None or y_data == None
    # animate = default_animate
    if (isDefault):
        ax = fig.add_subplot(xlim=(0, 2), ylim=(-1, 1))
    else:
        print("cleared")
        ax = fig.add_subplot(xlim=xlim, ylim=ylim)
        # animate = data_animate
    line, = ax.plot([], [], lw=2)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(column=0, row=0, rowspan=4, sticky="NSEW")
    anim = animation.FuncAnimation(
        fig, animate, init_func=init, frames=frames, interval=interval, blit=True)
    # plt.show()
    # plt.grid()

    canvas.draw()


def init():
    print("reseting....")
    line.set_data([], [])
    return line,


def animate(i):
    if (x_data == None):
        x = np.linspace(0, 2, 1000)
        y = np.sin(2 * np.pi * (x - 0.01 * i))
    else:

        print('have x_data')
        x = x_data[i]
        y = y_data[i]
        print(x, y)
    line.set_data(x, y)

    return line,
