from pyclbr import Function
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


plt.style.use('fivethirtyeight')

xval = []
yval = []
index = count()

def animate(i):
    xval.append(next(index))
    yval.append(random.randint(0,5))

    plt.cla()
    plt.plot(xval,yval)
ani = FuncAnimation(plt.gcf(),animate,interval=10)

plt.plot(xval,yval)
plt.tight_layout()
plt.show()