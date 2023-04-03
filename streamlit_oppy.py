import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from IPython import display
import warnings

#suppress warnings
warnings.filterwarnings('ignore')

def x_set(t):
    x1 = 1.5*np.exp((0.12*np.sin(t)-0.5)*(y+0.16*np.sin(t))**2)/(1+np.exp(-20*(5*y+np.sin(t))))
    x2 = (1.5+0.8*(y+0.2*np.sin(t))**3)*(1+np.exp(20*(5*y+np.sin(t))))**(-1)/(1+np.exp(-1*(100*(y+1)+16*np.sin(t))))
    x3 = 0.2*(np.exp(-1*(y+1)**2)+1)/(1+np.exp(100*(y+1)+16*np.sin(t)))
    x4 = 0.1/np.exp(2*(10*y+1.2*(2+np.sin(t))*np.sin(t))**4)

    x = x1 + x2 + x3 + x4
    x = x.astype(np.float64)
    return x


fig = plt.figure(figsize=(4,10))

frames = []
num_frames = 1000
for i in range(num_frames):
    frame = plt.plot(x_set(i*0.1), y)
    frames.append(frame)

# 描画
ani = ArtistAnimation(fig, frames, interval=10)
display.HTML(ani.to_jshtml())
# display.display(html)
# plt.close()
