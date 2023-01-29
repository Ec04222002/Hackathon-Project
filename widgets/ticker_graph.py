# import tkinter
# from matplotlib.backends.backend_tkagg import (
#     FigureCanvasTkAgg, NavigationToolbar2Tk)
# from matplotlib.backend_bases import key_press_handler
# from matplotlib import pyplot as plt, animation
# import numpy as np

# plt.rcParams["figure.figsize"] = [7.00, 3.50]
# plt.rcParams["figure.autolayout"] = True

# root = tkinter.Tk()
# root.wm_title("Embedding in Tk")


# class TickerGraph:
#     def __init__(self, root):
#         # self.x_data = x_data
#         # self.y_data = y_data
#         # self.x_label = x_label
#         # self.y_label = y_label
#         self.root = root

#         self.init_plt()
#         self.init_canvas()

#     def init_plt(self):
#         plt.axes(xlim=(0, 2), ylim=(-2, 2))

#         # plt.grid()
#         fig = plt.Figure(dpi=100)

#         ax = fig.add_subplot(xlim=(0, 2), ylim=(-1, 1))
#         line, = ax.plot([], [], lw=2)

#         self.fig = fig
#         self.ax = ax
#         self.line = line

#     def init_canvas(self):
#         canvas = FigureCanvasTkAgg(self.fig, master=self.root)
#         canvas.draw()

#         toolbar = NavigationToolbar2Tk(canvas, self.root, pack_toolbar=False)
#         toolbar.update()

#         canvas.mpl_connect(
#             "key_press_event", lambda event: print(f"you pressed {event.key}"))
#         canvas.mpl_connect("key_press_event", key_press_handler)
#         self.canvas = canvas

#     def frame_animate(self, i):
#         x = np.linspace(0, 2, 1000)
#         y = np.sin(2 * np.pi * (x - 0.01 * i))
#         self.line.set_data(x, y)
#         return self.line,

#     def animate_init(self):
#         self.line.set_data([], [])
#         return self.line,

#     def animate(self):

#         anim = animation.FuncAnimation(
#             self.fig, self.frame_animate, init_func=self.animate_init, frames=200, interval=20, blit=True)

#         plt.grid()
#         plt.show()


import tkinter
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib import pyplot as plt, animation
import numpy as np

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

# root = tkinter.Tk()
# root.wm_title("Embedding in Tk")


def draw(root):
    global fig, line
    plt.axes(xlim=(0, 2), ylim=(-2, 2))
    fig = plt.Figure(dpi=100)
    ax = fig.add_subplot(xlim=(0, 2), ylim=(-1, 1))
    line, = ax.plot([], [], lw=2)

    canvas = FigureCanvasTkAgg(fig, master=root)

    canvas.get_tk_widget().pack()
    anim = animation.FuncAnimation(
        fig, animate, init_func=init, frames=200, interval=20, blit=True)
    # plt.show()
    canvas.draw()


def init():
    line.set_data([], [])
    return line,


def animate(i):
    print(i)
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)

    return line,
