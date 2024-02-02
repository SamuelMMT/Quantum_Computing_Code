import numpy as np
from gates import XGate, YGate, ZGate, HGate
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

last_qubit_state = None

def init_bloch_sphere():
    # Initialize the Bloch sphere representation
    fig = plt.figure()
    ax = fig.add_subplot(111, projection = "3d")
    
    #Draw sphere with radius 1
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.cos(u)*np.sin(v)
    y = np.sin(u)*np.sin(v)
    z = np.cos(v)
    ax.plot_wireframe(x, y, z, color='gray', alpha=0.5)
    
    # Setting the axes properties
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    
    #initial state - arrow pointing towards the state
    qubit_state = ax.quiver(0, 0, 0, 0, 0, 1, color='blue', arrow_length_ratio=0.1)
    return fig, ax, qubit_state

def update(frame, ax, qubit_state, gate_function):
    # Calculate the new position of the qubit state
    new_position = gate_function(frame)
    x, y, z = new_position

    # Remove the old arrow
    global last_qubit_state
    if last_qubit_state is not None:
        last_qubit_state.remove()

    # Create a new arrow pointing to the new position
    last_qubit_state = ax.quiver(0, 0, 0, x, y, z, color='blue', arrow_length_ratio=0.1)
    
    return last_qubit_state,




def animate_qubit_gate(gate_function, frames=100):
    fig, ax, qubit_state = init_bloch_sphere()
    ani = FuncAnimation(fig, update, frames=range(frames), fargs=(ax, qubit_state, gate_function), blit=False)
    plt.show()


# Example usage
x_gate = XGate()

# For a static application
x_gate_matrix = x_gate.get_matrix()

# For animation
x_gate_animation_function = x_gate.get_animation_function(total_frames=100)
animate_qubit_gate(x_gate_animation_function)

