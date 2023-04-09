
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
from matplotlib.animation import FuncAnimation
from IPython import display

def x_set(t, y, R18_flag):

    x1 = 1.5*np.exp((0.12*np.sin(t)-0.5)*(y+0.16*np.sin(t))**2)/(1+np.exp(-20*(5*y+np.sin(t))))
    x2 = (1.5+0.8*(y+0.2*np.sin(t))**3)*(1+np.exp(20*(5*y+np.sin(t))))**(-1)/(1+np.exp(-1*(100*(y+1)+16*np.sin(t))))
    x3 = 0.2*(np.exp(-1*(y+1)**2)+1)/(1+np.exp(100*(y+1)+16*np.sin(t)))
    x4 = 0.1/np.exp(2*(10*y+1.2*(2+np.sin(t))*np.sin(t))**4)

    if R18_flag:
        x = x1 + x2 + x3 + x4
    else:
        x = x1  + x2 +  x3
#     x = x.astype(np.float64)
    return x

# Streamlit app
def app_ver1():
    st.title('BAIN')
    speed = st.slider('BAIN SPEED', 0, 10, 5, 1)
    st.text("あなたは18歳以上ですか？")
    R18_flag = st.checkbox("私は18歳以上です。")

    fig = plt.figure(figsize=(3,8))
    y = np.linspace(-3, 3, 100)
    frames = []
    num_frames = 100
    for i in range(num_frames):
        frame = plt.plot(x_set(i*0.1, y, R18_flag), y, color="black")
        frames.append(frame)

    # 描画
    ani = ArtistAnimation(fig, frames, interval=110-speed*10)
    components.html(ani.to_jshtml(), height=2000)

def update(i,y,py_line,R18_flag):

    x = x_set(i, y, R18_flag)
    py_line.set_data(x,y)

def app_ver2():
    st.title('BAIN')
    speed = st.slider('BAIN SPEED', 0, 10, 5, 1)
    st.text("あなたは18歳以上ですか？")
    R18_flag = st.checkbox("私は18歳以上です。")

    fig,ax = plt.figure(figsize=(3,8))
    py_line, = ax.plot([],[])

    ax.set_xlim(0, 1.7)
    ax.set_ylim(-3, 3)

    y = np.linspace(-3, 3, 100)

    # 描画　高速化
    anim = FuncAnimation(fig, update(y, py_line, R18_flag))
    components.html(anim.to_jshtml(), height=2000)

# Run the app
if __name__ == '__main__':
    app_ver2()
