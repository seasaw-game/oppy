import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from IPython import display
import warnings

#suppress warnings
warnings.filterwarnings('ignore')


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
