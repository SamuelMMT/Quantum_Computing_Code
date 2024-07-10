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

    def get_animation_function(self, total_frames):
        def apply_y_gate_over_time(frame):
            angle = np.pi * (frame / total_frames)
            x = np.cos(angle)
            y = np.sin(angle)
            z = 0
            return x, y, z
        return apply_y_gate_over_time


class ZGate:
    def get_matrix(self):
        return np.array([[1, 0], [0, -1]])

    def get_animation_function(self, total_frames):
        def apply_z_gate_over_time(frame):
            angle = np.pi * (frame / total_frames)
            x = 1 * np.cos(angle)  # Assume starting at |+⟩ for visualization
            y = 1 * np.sin(angle)
            z = 0
            return x, y, z
        return apply_z_gate_over_time


class HGate:
    def get_matrix(self):
        return np.array([[1, 1], [1, -1]]) / np.sqrt(2)

    def get_animation_function(self, total_frames):
        def apply_h_gate_over_time(frame):
            angle = (np.pi/2) * (frame / total_frames)  # Rotate from |0⟩ to |+⟩
            x = np.cos(angle)
            y = 0
            z = np.sin(angle)
            return x, y, z
        return apply_h_gate_over_time
