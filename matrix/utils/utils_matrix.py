import numpy as np

class Utils:
    def __init__(self) -> None:
        pass

    def initialize_matrix(self, size:int):
        matrix_a, matrix_b = self.__generate_random_matrix__(size), self.__generate_random_matrix__(size)
        output = np.zeros_like(matrix_a)
        return matrix_a, matrix_b, output
    
    def __check_matrix_dim__(self, matrix_a, matrix_b):
        if(matrix_a.shape != matrix_b.shape):
            raise AssertionError("sum: shapes should be equal.")
        return True
    
    def __join__threads__(self, threads:list):
        for t in threads:
            t.join()

    def __generate_random_matrix__(self, size:int):
        # low, high = -1024, 1024
        low, high = 0, 20
        return np.random.randint(size=size**2, low=low, high=high).reshape((-1, size))