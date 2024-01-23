#unit test for qubit.py

import pytest
from simulator.qubit import Qubit
import numpy as np

class TestQubit:
    def test_initialization(self):
        # Test the initialization of a qubit
        qubit = Qubit()
        assert np.isclose(qubit.alpha, 1)
        assert np.isclose(qubit.beta, 0)

    def test_normalization(self):
        # Test the normalization of qubit states
        qubit = Qubit(1 / np.sqrt(2), 1 / np.sqrt(2))
        assert np.isclose(abs(qubit.alpha)**2 + abs(qubit.beta)**2, 1)

    def test_bloch_representation(self):
        # Test the Bloch sphere representation
        qubit = Qubit(1, 0)  # |0> state
        x, y, z = qubit.bloch_representation()
        assert np.isclose(x, 0) and np.isclose(y, 0) and np.isclose(z, 1)

    def test_ket_representation(self):
        # Test the ket representation output
        qubit = Qubit(1, 0)
        ket_repr = qubit.ket_representation()
        assert ket_repr == "1.00|0⟩ + 0.00|1⟩"

    # Additional tests can be added here for other methods like measurement

# You can add more test cases as needed
