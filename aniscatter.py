from __future__ import division
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

import pickle

mfcc = pickle.load( open( "mfcc.p", "rb" ))
chroma = pickle.load(open("chroma.p", "rb"))
clicks = pickle.load(open("clicksonly.p","rb"))
mels = pickle.load(open("mel.p","rb"))

print(len(clicks))
mfcc = chroma[5]
mfcc2 = chroma[10]
print(len(mfcc))
# print(nonsense)
mfcc=list(mfcc)
framenum = int((22050/512)/10)
padnum = -(len(mfcc) - int(len(mfcc)/framenum) * framenum)
mfcc=mfcc[0:-2]
# for i in range(0,padnum):
# 	mfcc.append(0)
mfcc = np.array(mfcc)
mfccani = np.reshape(mfcc, (int(len(mfcc)/framenum), framenum))

mfcc2=list(mfcc2)
mfcc2 = mfcc2[0:-2]
# for i in range(0,padnum):
# 	mfcc2.append(0)
mfcc2 = np.array(mfcc2)
mfccani2 = np.reshape(mfcc2, (int(len(mfcc2)/framenum), framenum))

clicksframelen = 10
clicks = clicks[0:-2]
clicksani = np.reshape(clicks, (int(len(clicks)/clicksframelen) , clicksframelen))
# chromadict = {}
chromadictani = {} 
print(len(chroma))
for i in range(0,12):
	chromaindi = chroma[i]
	chromaindi = list(chromaindi)
	chromaindi = chromaindi[0:-2]
	# for j in range(0,69-42):
	# 	chromaindi.append(0)
	chromaindi = np.array(chromaindi)
	# chromadict[i] = chroma[i]
	chromadictani[i] = np.reshape(chromaindi,(int(len(mfcc2)/framenum), framenum))

print(chromadictani[1].shape)
print(chromadictani[2].shape)

x = np.random.randn(12,)
y = np.random.randn(12,)
Acc_11 = x
Acc_12 = y

# Scatter plot
fig = plt.figure(figsize = (5,5))
axes = fig.add_subplot(111)
axes.set_xlim(0,12)
axes.set_ylim(0,2)

point, = axes.plot(Acc_11,Acc_12, 'go')

# print(sum(chromadictani).shape)

def ani(coords):
    point.set_data([coords[0]],[coords[1]])
    return point

rect = plt.Rectangle((0,0), 2, 2, ec='none', lw=2)
def frames(self):
	clickstimes=int(len(y)/clicksframelen)
	print(clickstimes)
	j=0
	for clicksj in range(0, clickstimes):
		c = abs(np.random.rand(3,1))
		print(clicksj)
		point.set_markersize(sum(clicksani[clicksj+10])+1)
		if clicksj % int((len(clicks)/4410)) == 0:
			for i in range(0,12):
				x[i] = i
				y[i] = sum(chromadictani[i][j])/10
				j+=1
			point.set_data(x, y)
		
	# for j in range(0, 4410):
	rect.set_facecolor(c)
		# print(x, y)
	return point
    # for acc_11_pos, acc_12_pos in zip(Acc_11, Acc_12):
    #     yield acc_11_pos, acc_12_pos

ani = FuncAnimation(fig, frames, interval=10)

# import os
# import pygame
# pygame.mixer.init()
# pygame.mixer.music.load(" C:/Users/admin_local/Dropbox/music/test.m4a")
# pygame.mixer.music.play()
# import librosa
# librosa.Audio(data=y, rate=sr)
# os.system("start C:/Users/admin_local/Dropbox/music/test.m4a")
plt.show()
# ani.save_count = 4410
# ani.save('test.mp4',fps=20)