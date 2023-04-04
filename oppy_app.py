
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.animation import ArtistAnimation
from matplotlib.animation import FuncAnimation
from IPython import display


class BAIN:
    def __init__(self, speed):
        self.speed = speed

    def oppy_update(self, t):
        y = np.linspace(-3, 3, 100)
        x1 = 1.5*np.exp((0.12*np.sin(t)-0.5)*(y+0.16*np.sin(t))**2)/(1+np.exp(-20*(5*y+np.sin(t))))
        x2 = (1.5+0.8*(y+0.2*np.sin(t))**3)*(1+np.exp(20*(5*y+np.sin(t))))**(-1)/(1+np.exp(-1*(100*(y+1)+16*np.sin(t))))
        x3 = 0.2*(np.exp(-1*(y+1)**2)+1)/(1+np.exp(100*(y+1)+16*np.sin(t)))
        x4 = 0.1/np.exp(2*(10*y+1.2*(2+np.sin(t))*np.sin(t))**4)
        x = x1 + x2 + x3 + x4
        self.ax.cla()
        self.ax.plot(x,y, color="black")

    def animate(self):
        fig = plt.figure(figsize=(3,8))
        self.ax = fig.add_subplot(111)
        # y = np.linspace(-3, 3, 100)
        # frames = []
        # num_frames = 100
        # for i in range(num_frames):
        #     frame = plt.plot(self.x_set(i*0.1, y), y, color="black")
        #     frames.append(frame)

        # 描画
#         ani = ArtistAnimation(fig, frames, interval=110-self.speed*10)
        ani = FuncAnimation(fig, self.oppy_update, frames=range(1000), interval=110-self.speed*10)
        components.html(ani.to_jshtml(),height=800)

#         display.HTML(ani.to_jshtml())
#         display.display(html)
#         plt.close()

# Streamlit app
def app():
    st.title('BAIN')

    speed = st.slider('BAIN SPEED', 0, 10, 5, 1)

    # Create an instance of the BAIN class
    bain = BAIN(speed)

    # Display the animation
    bain.animate()

    # Display the matplotlib figure using st.pyplot
#     st.pyplot()

# Run the app
if __name__ == '__main__':
    app()
