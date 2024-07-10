import numpy as np

class Qubit:
    def __init__(self, alpha: complex = 1, beta: complex = 0):
        """
        Initialize a new Qubit with given alpha and beta coefficients.

        Args:
            alpha (complex): Amplitude for the |0⟩ state.
            beta (complex): Amplitude for the |1⟩ state.
        """
        self.alpha = complex(alpha)
        self.beta = complex(beta)
        self.normalize()

    def normalize(self) -> None:
        """
        Normalize the state vector to ensure that the sum of the squares of the coefficients is 1.
        """
        norm = np.sqrt(abs(self.alpha)**2 + abs(self.beta)**2)
        self.alpha /= norm
        self.beta /= norm

    def measure(self) -> int:
        """
        Simulate the measurement of the qubit, collapsing it to |0⟩ or |1⟩ based on the probabilities derived from the state amplitudes.

        Returns:
            int: The outcome of the measurement (0 for |0⟩ and 1 for |1⟩).
        """
        probabilities = [abs(self.alpha)**2, abs(self.beta)**2]
        outcome = np.random.choice([0, 1], p=probabilities)
        self.alpha, self.beta = (1, 0) if outcome == 0 else (0, 1)
        return outcome

    def bloch_sphere(self) -> tuple:
        """
        Calculate the coordinates of the qubit state on the Bloch sphere.

        Returns:
            tuple: Coordinates (x, y, z) representing the qubit on the Bloch sphere.
        """
        x = 2 * np.real(self.alpha * np.conj(self.beta))
        y = 2 * np.imag(self.alpha * np.conj(self.beta))
        z = abs(self.alpha)**2 - abs(self.beta)**2
        return x, y, z

    def ket_representation(self) -> str:
        """
        Provide the ket representation (Dirac notation) of the qubit state.

        Returns:
            str: The ket representation of the qubit.
        """
        alpha_repr = f"{self.alpha.real:.2f}" if self.alpha.imag == 0 else f"{self.alpha:.2f}"
        alpha_repr += "|0⟩ "
        beta_repr = f"{self.beta.real:.2f}" if self.beta.imag == 0 else f"{self.beta:.2f}"
        beta_repr += "|1⟩"
        ket_repr = alpha_repr + "+ " + beta_repr if self.beta.real >= 0 else "- " + beta_repr
        return ket_repr.strip()
    
    def apply_gate(self, gate: np.ndarray) -> None:
        """
        Apply a quantum gate to the qubit. The gate is represented by a 2x2 unitary matrix.

        Args:
            gate (np.ndarray): A 2x2 numpy array representing the quantum gate.
        """
        state_vector = np.array([self.alpha, self.beta])
        new_state_vector = np.dot(gate, state_vector)
        self.alpha, self.beta = new_state_vector[0], new_state_vector[1]
        self.normalize()
