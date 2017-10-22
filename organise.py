from __future__ import division
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

import pickle

mfcc = pickle.load( open( "mfcc.p", "rb" ))
chroma = pickle.load(open("chroma.p", "rb"))
clicks = pickle.load(open("clicksonly.p","rb"))
mels = pickle.load(open("mel.p","rb"))
beats = pickle.load(open("beats.p","rb"))

normmfcc = [feature / max(feature) for feature in mfcc]

sr = 22050
framenum = len(clicks) / len(chroma[0])
time = len(clicks)/sr
windowsize = 512
steplength = 512
interval = (time / (framenum))*1000
interval = (windowsize / sr) * 1000

np.set_printoptions(threshold="None")
# print(mels.shape)(128,16442)
# print(list(clicks).count(0)) = 6300228
# print(mfcc.shape) = (20,16442)

x = np.random.randn(12,)
y = np.random.randn(12,)
Acc_11 = x
Acc_12 = y

# Scatter plot
fig = plt.figure(figsize = (5,5))
axes = fig.add_subplot(111)
axes.set_xlim(0,12)
axes.set_ylim(0,2)

point, = axes.plot(Acc_11, Acc_12, 'go')
b=0

newbeats = list(beats)
def ani(t):
	for i in range(0,12):
		x[i] = i
		y[i] = chroma[i][t]
	point.set_data(x, y)

	global b
	if abs(t - beats[b]) == 0:
		point.set_markersize(20)
		b+=1
	else:
		point.set_markersize(10)

	c = (abs(normmfcc[0][t])/100, abs(normmfcc[1][t]/2), abs(normmfcc[2][t])/10)
	point.set_color(c)
	print(c)
 #    c = abs(np.random.rand(3,1))
	# for t in range(0, len(chroma)):

	return point

ani = FuncAnimation(fig, ani, interval=interval)

# plt.show()
ani.save_count = len(mfcc[0])
ani.save('test.mp4')