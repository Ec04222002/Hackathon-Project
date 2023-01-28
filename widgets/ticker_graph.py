import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from matplotlib.animation import FuncAnimation
import datetime as dt
import matplotlib.dates as mdates

class TickerGraph:

    def __init__(self, ticker_name, start_date, time_x, price_y):
        self.ticker_name = ticker_name
        self.start_date = start_date
        self.time_x = time_x
        self.price_y = price_y
        

    def make_graph(self):
      #x = ['1:30', '2:00', '2:30', '3:30', '4:00', '4:30', '5:00', '5:30',   '6:00', '6:30']
      y = [1, 2, 3, 4, 5, 6,7, 8, 9, 10]
      
      #fig = plt.figure()
      #plt.plot(x,y)
      #plt.xticks(np.arange(0,10,2))
      #plt.show()
      
      dates = ['01/02/1991','01/03/1991','01/04/1991']
      x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
      x_data = []
      y_data = []
      
      fig, ax = plt.subplots()
      ax.set_xlim(0, 105)
      ax.set_ylim(0,12)
      line, = ax.plot(0,0)
      
      plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
      plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval = 5))
      plt.gcf().autofmt_xdate()
      
      def animation_frame(i):
          x_data.append(x[int(i)])
          y_data.append(y[int(i)])
          
          line.set_xdata(x_data)
          line.set_ydata(y_data)
          return line,
      
      animation = FuncAnimation(fig, func=animation_frame, frames = np.arange(0, 10, 0.01), interval = 10)
      plt.show()
        
        
          
        
        pass
