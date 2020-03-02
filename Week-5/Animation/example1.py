# Uncomment the next two lines if you want to save the animation
#import matplotlib
#matplotlib.use("Agg")

import numpy
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.animation as animation
import seaborn as sns

sns.set(color_codes=True)

# Sent for figure
font = {'size'   : 9}
matplotlib.rc('font', **font)

# Setup figure and subplots
fig, ax = plt.subplots()
fig.set_size_inches(16,9)
#tight_layout()

# Set titles of subplots
ax.set_title('Position and Velocity vs Time')

# set y-limits
ax.set_ylim(0,0.1)

# sex x-limits
ax.set_xlim(0,0.1)

# Turn on grids
ax.grid(True)

# set label names
ax.set_xlabel("x")
ax.set_ylabel("y")

# Data Placeholders
y=zeros(0)
t=zeros(0)

# set plots
p, = ax.plot(t,y,'b-', label="abc")

# set lagends
ax.legend([p], [p.get_label()])

# Data Update
xmin = 0.0
xmax = 5.0
ymin = 0.0
ymax = 5.0
x = 0.0

def updateData(self):
	global t
	global x
	global y

	tmpp = 2**x
	y=append(y,tmpp)
	t=append(t,x)

	x += 0.05

	p.set_data(t,y)

	p.axes.set_xlim(0,x*10/9)

	p.axes.set_ylim(1,tmpp*10/9)

	return p

# interval: draw new frame every 'interval' ms
# frames: number of frames to draw
simulation = animation.FuncAnimation(fig, updateData, blit=False, frames=1000, interval=1, repeat=False)

# Uncomment the next line if you want to save the animation
simulation.save(filename='sim.mp4',fps=60,dpi=50)
