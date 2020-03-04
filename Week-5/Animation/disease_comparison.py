# Uncomment the next two lines if you want to save the animation
import matplotlib
matplotlib.use("Agg")

import numpy as np
from matplotlib.pylab import *
from mpl_toolkits.axes_grid1 import host_subplot
import matplotlib.animation as animation
import seaborn as sns

import pandas as pd

from scipy.interpolate import make_interp_spline, BSpline

from swine import Swine
from corona import Corona
from sars import Sars
from ebola import Ebola

from progress.bar import ChargingBar


## Init Progress bar
bar = ChargingBar('Rendering', max=2500,
	suffix='Frames Rendered: %(index)d/%(max)d -- elapsed: %(elapsed)ds -- eta: %(eta)ds')


sns.set(color_codes=True)

# Data Placeholders

# Swine
swine = Swine()

# Sars
sars = Sars()

# Corona
corona = Corona()

# Ebola
ebola = Ebola()




# Sent for figure
font = {'size'   : 9}
matplotlib.rc('font', **font)

# Setup figure and subplots
f0 = figure(num = 0, figsize = (16, 9))#, dpi = 100)
f0.suptitle("Disease Comparison", fontsize=12)
ax0 = subplot2grid((4, 4), (0, 0), colspan=4, rowspan=3)
ax1 = subplot2grid((4, 4), (3, 0), colspan=1, rowspan=1)
ax2 = subplot2grid((4, 4), (3, 1), colspan=1, rowspan=1)
ax3 = subplot2grid((4, 4), (3, 2), colspan=1, rowspan=1)
ax4 = subplot2grid((4, 4), (3, 3), colspan=1, rowspan=1)
#tight_layout()

# Set titles of subplots
ax1.set_title('Corona Death Ratio')
ax2.set_title('Ebola Death Ratio')
ax3.set_title('Swine Death Ratio')
ax4.set_title('Sars Death Ratio')

# Turn on grids
ax0.grid(True)
ax1.grid(False)
ax2.grid(False)
ax3.grid(False)
ax4.grid(False)

# Set label names
ax0.set_xlabel("Days")
ax0.set_ylabel("Cases")

# Set plots

### Smooth plot space
space = np.linspace(0, 20, 2001) 


# Pie Chart Label
labels = 'Death', 'Alive'
colors = ['r', 'g']

# Corona

spl = make_interp_spline(corona.get_cases()['Days'].values, corona.get_cases()['Cases'].values)
corona_case_smooth = spl(space)

spl = make_interp_spline(corona.get_deaths()['Days'].values, corona.get_deaths()['Deaths'].values)
corona_deaths_smooth = spl(space)

p_corona_line, = ax0.plot(space, corona_case_smooth,'b-', label="Corona")
p_corona_dot = ax0.scatter(corona.get_cases()['Days'].values, corona.get_cases()['Cases'].values,c='b')
ax1.pie([corona_deaths_smooth[1], corona_case_smooth[1] - corona_deaths_smooth[1]],
	labels=labels,
	colors=colors,
	autopct='%1.1f%%',
	startangle=90)

# Ebola

spl = make_interp_spline(ebola.get_cases()['Days'].values, ebola.get_cases()['Cases'].values)
ebola_case_smooth = spl(space)

spl = make_interp_spline(ebola.get_deaths()['Days'].values, ebola.get_deaths()['Deaths'].values)
ebola_deaths_smooth = spl(space)

p_ebola_line, = ax0.plot(space, ebola_case_smooth,'g-', label="Ebola")
p_ebola_dot = ax0.scatter(ebola.get_cases()['Days'].values, ebola.get_cases()['Cases'].values,c='g')
ax2.pie([ebola_deaths_smooth[1], ebola_case_smooth[1] - ebola_deaths_smooth[1]],
	labels=labels,
	colors=colors,
	autopct='%1.1f%%',
	startangle=90)

# Swine

spl = make_interp_spline(swine.get_cases()['Days'].values, swine.get_cases()['Cases'].values)
swine_case_smooth = spl(space)

spl = make_interp_spline(swine.get_deaths()['Days'].values, swine.get_deaths()['Deaths'].values)
swine_deaths_smooth = spl(space)

p_swine_line, = ax0.plot(space, swine_case_smooth,'r-', label="Swine")
p_swine_dot = ax0.scatter(swine.get_cases()['Days'].values, swine.get_cases()['Cases'].values,c='r')
ax3.pie([swine_deaths_smooth[1], swine_case_smooth[1] - swine_deaths_smooth[1]],
	labels=labels,
	colors=colors,
	autopct='%1.1f%%',
	startangle=90)

# Sars

spl = make_interp_spline(sars.get_cases()['Days'].values, sars.get_cases()['Cases'].values)
sars_case_smooth = spl(space)

spl = make_interp_spline(sars.get_deaths()['Days'].values, sars.get_deaths()['Deaths'].values)
sars_deaths_smooth = spl(space)

p_sars_line, = ax0.plot(space, sars_case_smooth,'y-', label="Sars")
p_sars_dot = ax0.scatter(sars.get_cases()['Days'].values, sars.get_cases()['Cases'].values,c='y')
ax4.pie([sars_deaths_smooth[1], sars_case_smooth[1] - sars_deaths_smooth[1]],
	labels=labels,
	colors=colors,
	autopct='%1.1f%%',
	startangle=90)


# p021, = ax02.plot(t,yv1,'b-', label="yv1")
# p022, = ax02.plot(t,yv2,'g-', label="yv2")

# p031, = ax03.plot(t,yp1,'b-', label="yp1")
# p032, = ax04.plot(t,yv1,'g-', label="yv1")

# set lagends
ax0.legend([p_corona_line, p_ebola_line, p_swine_line, p_sars_line],
	[p_corona_line.get_label(), p_ebola_line.get_label(), p_swine_line.get_label(), p_sars_line.get_label()])

ax0.xaxis.tick_top()

for n in (corona, sars, ebola, swine):
	for i, cases in enumerate(n.get_cases()['Cases'].values):
		ax0.annotate(cases, (n.get_cases()['Days'].values[i], cases))

# Data Update
x = 0.0

def updateData(self):
	
	global x
	global bar
	global p_corona_line
	global p_swine_line
	global p_sars_line
	global p_ebola_line

	global corona_deaths_smooth
	global corona_case_smooth
	global ebola_deaths_smooth
	global ebola_case_smooth
	global swine_deaths_smooth
	global swine_case_smooth
	global sars_deaths_smooth
	global sars_case_smooth


	global ax0

	if x < 20:
		x += 0.01

	p_corona_line.axes.set_ylim(0, max(corona_case_smooth[round(x*100)],
		ebola_case_smooth[round(x*100)],
		swine_case_smooth[round(x*100)],
		sars_case_smooth[round(x*100)])*10/9)
	p_corona_line.axes.set_xlim(0, x)

	ax1.set_title('Corona Death Ratio')
	ax2.set_title('Ebola Death Ratio')
	ax3.set_title('Swine Death Ratio')
	ax4.set_title('Sars Death Ratio')

	ax1.clear()
	ax1.pie([corona_deaths_smooth[round(x*100)], corona_case_smooth[round(x*100)] - corona_deaths_smooth[round(x*100)]],
		labels=labels,
		colors=colors,
		autopct='%1.1f%%',
		startangle=90)
	ax2.clear()
	ax2.pie([ebola_deaths_smooth[round(x*100)], ebola_case_smooth[round(x*100)] - ebola_deaths_smooth[round(x*100)]],
		labels=labels,
		colors=colors,
		autopct='%1.1f%%',
		startangle=90)
	ax3.clear()
	ax3.pie([swine_deaths_smooth[round(x*100)], swine_case_smooth[round(x*100)] - swine_deaths_smooth[round(x*100)]],
		labels=labels,
		colors=colors,
		autopct='%1.1f%%',
		startangle=90)
	ax4.clear()		
	ax4.pie([sars_deaths_smooth[round(x*100)], sars_case_smooth[round(x*100)] - sars_deaths_smooth[round(x*100)]],
		labels=labels,
		colors=colors,
		autopct='%1.1f%%',
		startangle=90)


	bar.next()

	return p_corona_line

# interval: draw new frame every 'interval' ms
# frames: number of frames to draw
simulation = animation.FuncAnimation(f0, updateData, blit=False, frames=2500, interval=1, repeat=False)

# Uncomment the next line if you want to save the animation
simulation.save(filename='animation.mp4', fps=60, dpi=150)

bar.finish()



