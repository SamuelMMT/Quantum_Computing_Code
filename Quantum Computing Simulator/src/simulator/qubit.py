import numpy as np


class Qubit:
    def __init__(self, alpha = 1, beta = 0):
        self.alpha = complex(alpha)
        self.beta = (beta)
        self.normalize()
        
    def normalize(self):
        #normalizing the vector by deviding it through the norm and therefor
        #maxing sure the sum of the square of the complex coeefficients is
        #always one
        norm = np.sqrt(abs(self.alpha)**2 + abs(self.beta)**2)
        self.alpha /= norm
        self.beta /= norm
    def measure(self):
        #simulate the measurement and collapse to state to a classical one
        probabilities = [abs(self.alpha)**2, abs(self.beta)**2]
    def bloch_sphere(self):
        x = 2*np.real(self.alpha * np.conj(self.beta))
        y = 2*np.real(self.alpha * np.conj(self.beta))
        z = abs(self.alpha)**2 - abs(self.beta)**2
        
        return x,y,z
    
    def ket_representation(self):
        #Dirac-Notation
        # Format alpha with precision and exclude the imaginary part if it's zero
        alpha_repr = f"{self.alpha.real:.2f}" if self.alpha.imag == 0 else f"{self.alpha:.2f}"
        alpha_repr += "|0⟩ "
        
        # Format beta similarly
        beta_repr = f"{self.beta.real:.2f}" if self.beta.imag == 0 else f"{self.beta:.2f}"
        beta_repr += "|1⟩"
        
        # Construct the full ket representation
        ket_repr = alpha_repr + "+ " + beta_repr if self.beta >= 0 else "- " + beta_repr
        return ket_repr.strip()
    
    def apply_gate(self, gate):
        "Apply a quantum gate to the qubit"
        state_vector = np.array([self.alpha, self.beta])
        new_state_vector = np.dot(gate, state_vector)
        self.alpha, self.beta = new_state_vector[0], new_state_vector[1]
        self.normalize()