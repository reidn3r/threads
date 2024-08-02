import numpy as np

def generate_random_matrix(size:int):
    low, high = -1024, 1024
    return np.random.randint(size=size**2, low=low, high=high).reshape((-1, size))