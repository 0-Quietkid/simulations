import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
A_x = 1
A_y = 1  
omega1 = int(input("Enter the frequency  for first SHM: "))
omega2 =int(input("Enter the frequency for second SHM: "))  
delta = int(input("Enter the phase difference: "))

t = np.linspace(0, 5, 300)

x = A_x * np.cos(omega1 * t)
y = A_y * np.cos(omega2 * t + delta)

fig, ax = plt.subplots()
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Lissajous Figure: Two Perpendicular SHM")

line, = ax.plot([], [], 'r-', lw=2)
point, = ax.plot([], [], 'bo')

def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

def update(frame):
    line.set_data(x[:frame], y[:frame])
    point.set_data([x[frame]], [y[frame]])
    return line, point

ani = animation.FuncAnimation(fig, update, frames=len(t), init_func=init, blit=False, interval=20)

# from IPython.display import HTML
# HTML(ani.to_jshtml())

plt.show()