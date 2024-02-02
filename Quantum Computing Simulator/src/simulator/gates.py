import numpy as np

class XGate:
    def get_matrix(self):
        return np.array([[0, 1], [1, 0]])
    def get_animation_function(self, total_frames):
        # Return a function that describes the gate's effect over time
        def apply_x_gate_over_time(frame):
            angle = np.pi * (frame / total_frames)
            x = np.sin(angle)
            y = 0
            z = np.cos(angle)
            return x, y, z
        return apply_x_gate_over_time

class YGate:
    def get_matrix(self):
        return np.array([[0, -1j], [1j, 0]])

    #add animation

class ZGate:
    def get_matrix(self):
        return np.array([[1, 0], [0, -1]])

    #add animation

class HGate:
    def get_matrix(self):
        return np.array([[1, 1], [1, -1]]) / np.sqrt(2)

    #add animation