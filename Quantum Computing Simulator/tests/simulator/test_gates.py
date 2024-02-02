from src.simulator.gates import XGate, YGate, ZGate, HGate
from src.simulator.qubit import Qubit
import numpy as np

x_gate = XGate()
y_gate = YGate()
z_gate = ZGate()
h_gate = HGate()

def test_x_gate():
    initial_state = Qubit(1, 0)
    initial_state.apply_gate(x_gate.get_matrix())
    assert np.isclose(initial_state.alpha, 0)
    assert np.isclose(initial_state.beta, 1)

def test_h_gate():
    initial_state = Qubit(1, 0)
    initial_state.apply_gate(h_gate.get_matrix())
    assert np.isclose(initial_state.alpha, 1 / np.sqrt(2))
    assert np.isclose(initial_state.beta, 1 / np.sqrt(2))

def test_z_gate():
    initial_state = Qubit(1, 0)
    initial_state.apply_gate(z_gate.get_matrix())
    assert np.isclose(initial_state.alpha, 1)
    assert np.isclose(initial_state.beta, 0)

def test_y_gate():
    initial_state = Qubit(1, 0)
    initial_state.apply_gate(y_gate.get_matrix())
    assert np.isclose(initial_state.alpha, 0)
    assert np.isclose(initial_state.beta, 1j)
  

