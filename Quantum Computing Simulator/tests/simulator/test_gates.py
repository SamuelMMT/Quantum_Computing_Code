from src.simulator.gates import x_gate, h_gate, y_gate, z_gate
from src.simulator.qubit import Qubit
import numpy as np

def test_x_gate():
    initial_state = Qubit(1,0) #|0> state
    initial_state.apply_gate(x_gate())
    assert np.isclose(initial_state.alpha, 0)
    assert np.isclose(initial_state.beta, 1)

def test_h_gate():
    initial_state = Qubit(1,0) #|0> state
    initial_state.apply_gate(h_gate())
    assert np.isclose(initial_state.alpha, 1/np.sqrt(2))
    assert np.isclose(initial_state.beta, 1/np.sqrt(2))
    
def test_z_gate():
    initial_state = Qubit(1,0) #|0> state
    initial_state.apply_gate(z_gate()) #should leave it
    assert np.isclose(initial_state.alpha, 1)
    assert np.isclose(initial_state.beta, 0)
    
def test_y_gate():
    initial_state = Qubit(1,0) #|0> state
    initial_state.apply_gate(y_gate()) #should send it to 
    assert np.isclose(initial_state.alpha, 0)
    assert np.isclose(initial_state.beta, 1j)    

