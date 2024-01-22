import numpy as np

class qubit:
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
        alpha_repr = f"{self.alpha: .2f}|0⟩ "
        beta_repr = f"+ {self.beta:.2f}|1⟩" if self.beta >= 0 else f"- {-self.beta:.2f}|1⟩"
        return alpha_repr + beta_repr