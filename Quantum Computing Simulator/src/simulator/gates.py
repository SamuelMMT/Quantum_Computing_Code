import numpy as np

def x_gate():
    "Apply X-Gate in the form of a matrix"
    return np.array([[0,1],[1,0]])

def y_gate():
    return np.array([[0, -1j],[1j,0]])

def z_gate():
    return np.array([[1,0],[0,-1]])

def h_gate():
    return np.array([[1,1],[1,-1]])/ np.sqrt(2)