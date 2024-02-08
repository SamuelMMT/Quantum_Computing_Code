import matplotlib.pyplot as plt
import numpy as np
import pennylane as qml
from qiskit import QuantumCircuit, transpile, execute, Aer
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
from IPython.display import display
import cirq
from cirq.contrib.svg import SVGCircuit
from PIL import Image
from cirq_web import bloch_sphere
"""
#with n qubits we are able to represent 2^n-1 states

PennyLane's standard for encoding numbers in a binary format. 
A binary number can be represented as a string of 1s and 0s, which we can represent as the multi-qubit state |m⟩ = |q0q1...qn-1⟩, 
where the formula to obtain the equivalent decimal number m will be: 

m = Σ (from i=0 to n-1) of 2^(n-1-i) * qi.

Note that |m⟩ refers to the basic state generated by the binary encoding of the number m. 
For instance, the natural number 6 is represented by the quantum state |110⟩, since 

|110⟩ = 1 * 2^2 + 1 * 2^1 + 0 * 2^0 = 6.
"""

#Lets represent integers using a computational basis with 3 seperate bloch's spheres
def print_rep_int():
    # Set up the figure and axes for the subplots
    num_states = 8
    num_cols = 4  # Define how many columns of subplots you want
    num_rows = (num_states + num_cols - 1) // num_cols  # Calculate the number of rows needed

    # Create a list to store the paths of the saved images
    bloch_sphere_images = []

    for i in range(num_states):
        # Create a quantum circuit with 3 qubits
        qc = QuantumCircuit(3)
        
        # Set the initial state of the qubits to represent the integer in its binary form
        binary_state = format(i, '03b')
        for qubit, bit in enumerate(binary_state):
            if bit == '1':
                qc.x(qubit)
        
        # Simulate the statevector
        statevector = Statevector.from_instruction(qc)
        
        # Plot the Bloch spheres and save to a file
        plot_filename = f'bloch_sphere_{i}.png'
        plot_bloch_multivector(statevector).savefig(plot_filename)
        plt.close()  # Close the figure to prevent it from displaying
        bloch_sphere_images.append(plot_filename)

    # Create a new figure for the combined subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(3 * num_cols, 3 * num_rows))

    # Remove the axes for the empty subplots
    for ax in axes.flatten()[num_states:]:
        ax.remove()

    # Load and display the Bloch sphere images on the subplots
    for i, plot_filename in enumerate(bloch_sphere_images):
        img = Image.open(plot_filename)
        ax = fig.add_subplot(num_rows, num_cols, i+1)
        ax.imshow(img)
        ax.axis('off')  # Hide the axes
        ax.set_title(f"Integer {i}")

    # Adjust the layout to prevent overlapping
    plt.tight_layout()

    # Show the combined plot
    plt.show()

#pennylane example for representing integer 6
def penny_int():
    dev = qml.device("default.qubit", wires=3)

    @qml.compile
    @qml.qnode(dev)
    def basis_embedding_circuit(m):
        qml.BasisEmbedding(m, wires=range(3))
        return qml.state()

    m = 6 # number to be encoded

    qml.draw_mpl(basis_embedding_circuit, show_all_wires=True)(m)
    plt.show()

def fourier_basis_visualization():
    #alpha_j = (2*m*pi)/2^j
    #represent integers by rotating them in the XY-basis
    # Set up the figure and axes for the subplots
    num_states = 8
    num_qubits = 3  # Define the number of qubits
    plots = [] 

    # Create a list to store the paths of the saved images
    bloch_sphere_images = []

    for m in range(num_states):
        # Create a quantum circuit with 3 qubits
        qc = QuantumCircuit(num_qubits)
        
        # Set the initial state of the qubits to represent the integer in its binary form
        binary_state = format(m, f'0{num_qubits}b') #e.g for m = 0 is binary_state 000
        for j in range(num_qubits):
            phi = (2*m*np.pi)/2**(j+1)
            #bring each qubit in superposition
            qc.h(j)
            #apply phase shift with Rz according to Fourier
            qc.p(phi, j)
            
        # Simulate the statevector
        statevector = Statevector.from_instruction(qc)
        
        # Plot the Bloch spheres for visualization
        plot = plot_bloch_multivector(statevector)
        plots.append(plot)

    # Display the plots in a single figure with subplots
    fig, axes = plt.subplots(2, 4, figsize=(15, 6))
    for i in range(8):
        plots[i].savefig(f'bloch_sphere_{i}.png')
        img = plt.imread(f'bloch_sphere_{i}.png')
        axes[i // 4, i % 4].imshow(img)
        axes[i // 4, i % 4].axis('off')
        axes[i // 4, i % 4].set_title(f"Integer {i}")

    plt.tight_layout()
    plt.show()


def rotate_xy_and_plot(qc, qubit, theta, phi):
    # Function to add rotation and plot the state at each step
    
    # Initial state
    state = execute(qc, Aer.get_backend('statevector_simulator')).result().get_statevector()
    plot_bloch_multivector(state, title="Initial State")
    plt.show()
    
    # Rotate around Z-axis by phi
    qc.rz(phi, qubit)
    state = execute(qc, Aer.get_backend('statevector_simulator')).result().get_statevector()
    plot_bloch_multivector(state, title=f"After Rz({phi})")
    plt.show()
    
    # Rotate around X-axis by theta
    qc.rx(theta, qubit)
    state = execute(qc, Aer.get_backend('statevector_simulator')).result().get_statevector()
    plot_bloch_multivector(state, title=f"After Rx({theta})")
    plt.show()
    
    # Rotate back around Z-axis by -phi
    qc.rz(-phi, qubit)
    state = execute(qc, Aer.get_backend('statevector_simulator')).result().get_statevector()
    plot_bloch_multivector(state, title=f"After Rz({-phi})")
    plt.show()




if __name__ == "__main__":
    #print_rep_int()
    penny_int()

    #visualize what Rz and Rx do
    # Create a quantum circuit with one qubit
    qc = QuantumCircuit(1)

    # Set rotation angles
    theta = np.pi / 2  # 90 degree rotation
    phi = np.pi / 4    # 45 degree phase shift

    # Apply the rotation and plot at each step
    rotate_xy_and_plot(qc, 0, theta, phi)
    
    fourier_basis_visualization()
#Basic arithmetic with the quantum Fourier transform (QFT)¶