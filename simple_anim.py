"""
A simple example of an animated plot
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import pickle

mfcc = pickle.load( open( "mfcc.p", "rb" ))
chroma = pickle.load(open("chroma.p", "rb"))
clicks = pickle.load(open("clicks.p","rb"))
mels = pickle.load(open("mel.p","rb"))

fig, ax = plt.subplots()

# print(mfcc, len(mfcc), max(mfcc),min(mfcc))
# print(chroma, len(chroma[0]), max(chroma[0]),min(chroma[0]))
# print(clicks,len(clicks),max(clicks),min(clicks))
# print(mels,len(mels[0]),max(mels[0]),min(mels[0]))

mfcc = clicks
# x = np.arange(0, 2*np.pi, 0.01)
# y = x
# line, = ax.plot(x, np.sin(x))

x = np.random.randn(100,1)
y = np.random.randn(100,1)
point, = ax.plot([x[0]],[y[0]], 'go')

mfcc=list(mfcc)
for i in range(0,8418300-8418272):
	mfcc.append(0)

mfcc = np.array(mfcc)
print(sum(mfcc))
mfccani = np.reshape(mfcc, (int(len(mfcc)/50), 50))
print(len(mfccani[0]))

def animate(i):
    # line.set_ydata(np.sin(x + i/10.0))  # update the data
    dots.set_ydata((x + i * sum(mfccani[i])))
    print(sum(mfccani[i]))
    return dots

def ani(coords):
    point.set_data([coords[0]],[coords[1]])
    return point

def frames():[
    for acc_11_pos, acc_12_pos in zip(x[0], y[0]):
        yield acc_11_pos, acc_12_pos

# Init only required for blitting to give a clean slate.
def init():
    dots.set_ydata(np.ma.array(x, mask=True))
    return dots

ani = FuncAnimation(fig, ani, np.arange(1, 100), frames = frames, interval=20, blit=True)
# plt.show()
ani.save('test.mp4', fps=15)
