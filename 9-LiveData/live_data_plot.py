from matplotlib import pyplot as plt
import pandas as pd
from itertools import count
import random
from matplotlib.animation import FuncAnimation

plt.style.use('ggplot')

x_vals = []
y_vals = []

index = count()

# Plotting by using count() function and random numbers from 0 to 5.

#plt.plot(x_vals, y_vals)
#def animate(i):
#    x_vals.append(next(index))
#    y_vals.append(random.randint(0,5))
#    plt.cla()
#    #print(x_vals,y_vals)
#    plt.plot(x_vals,y_vals)

def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y1 = data ['total_1']
    y2 = data ['total_2']

    plt.cla()

    plt.plot(x, y1, label='Channel 1')
    plt.plot(x, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval= 1000)

plt.tight_layout()
plt.show()
