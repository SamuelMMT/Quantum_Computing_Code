import numpy as np
from gates import XGate, YGate, ZGate, HGate
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

last_qubit_state = None  # Global variable to track the last state of the quiver

def init_bloch_sphere():
    """Initializes and returns the Bloch sphere with an initial state arrow."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    
    # Draw sphere with radius 1
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)
    ax.plot_wireframe(x, y, z, color='gray', alpha=0.5)
    
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    qubit_state = ax.quiver(0, 0, 0, 0, 0, 1, color='blue', arrow_length_ratio=0.1)
    return fig, ax, qubit_state

def update(frame, ax, qubit_state, gate_function):
    """Updates the qubit state in the animation."""
    new_position = gate_function(frame)
    x, y, z = new_position

    global last_qubit_state
    if last_qubit_state is not None:
        last_qubit_state.remove()

    last_qubit_state = ax.quiver(0, 0, 0, x, y, z, color='blue', arrow_length_ratio=0.1)
    return last_qubit_state,

def animate_qubit_gate(gate_function, frames=100):
    """Animates the effect of a quantum gate on the qubit."""
    fig, ax, qubit_state = init_bloch_sphere()
    ani = FuncAnimation(fig, update, frames=range(frames), fargs=(ax, qubit_state, gate_function), blit=False)
    plt.show()

# Example usage
x_gate = XGate()
x_gate_animation_function = x_gate.get_animation_function(total_frames=100)
animate_qubit_gate(x_gate_animation_function)
