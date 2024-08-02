import threading
import numpy as np
from utils.generate_matrix import generate_random_matrix

class MatrixSum:
    def __init__(self):
        pass

    def sum_matrix_sequential(self, matrix_a, matrix_b, output, start_column=None, end_column=None):
        self.__check_matrix_dim__(matrix_a, matrix_b)
        
        start_column = 0 if start_column is None else start_column
        end_column = matrix_a.shape[1] if end_column is None else end_column

        
        for i in range(output.shape[0]):
            for j in range(start_column, end_column):
                output[i][j] = matrix_a[i][j] + matrix_b[i][j]

    def sum_matrix_parallel(self, n_threads:int, matrix_a, matrix_b, output):
        n_cols:int = matrix_a.shape[1]
        column_thread_ratio:int = n_cols // n_threads
        threads = []
        for i in range(n_threads):
            start_column:int = i * column_thread_ratio
            # end_column:int = n_cols if i == n_threads - 1 else start_column + column_thread_ratio
            end_column:int = (i+1) * column_thread_ratio if i != n_threads - 1 else n_cols
            
            thread = threading.Thread(target=self.sum_matrix_sequential, args=(matrix_a, matrix_b, output, start_column, end_column))
            threads.append(thread)
            thread.start()
    
        self.__join__threads__(threads)

        # print(matrix_a)
        # print("\n")

        # print(matrix_b)
        # print("\n")
        
        # print(output)
        return output


    def initialize_matrix(self, size:int):
        matrix_a, matrix_b = generate_random_matrix(size), generate_random_matrix(size)
        output = np.zeros_like(matrix_a)
        return matrix_a, matrix_b, output
    
    def __check_matrix_dim__(self, matrix_a, matrix_b):
        if(matrix_a.shape != matrix_b.shape):
            raise AssertionError("sum: shapes should be equal.")
        return True
    
    def __join__threads__(self, threads:list):
        for t in threads:
            t.join()
