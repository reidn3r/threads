import threading
import numpy as np
from utils.utils_matrix import Utils

class MatrixMultiply(Utils):

    def __init__(self) -> None:
        pass

    def multiply_matrix_sequential(self, matrix_a, matrix_b, output, start_column=None, end_column=None):
        n_rows:int = matrix_a.shape[0]

        start_column = 0 if start_column is None else start_column
        end_column = matrix_a.shape[1] if end_column is None else end_column

        for i in range (n_rows):
            for j in range (start_column, end_column):
                output[i][j] = 0
                for k in range(n_rows):
                    output[i][j] += matrix_a[i][k] * matrix_b[k][j]


    # def multiply_matrix_parallel(self, n_threads:int, matrix_a, matrix_b, output):
    #     n_cols:int = matrix_a.shape[1]
    #     n_threads = min(n_threads, matrix_a.shape[1])
    #     column_thread_ratio:int = n_cols // n_threads
    #     threads = []
        
    #     for i in range(n_threads):
    #         start_column:int = i * column_thread_ratio
    #         end_column:int = (i+1) * column_thread_ratio if i != n_threads - 1 else n_cols
            
    #         thread = threading.Thread(target=self.multiply_matrix_sequential, args=(matrix_a, matrix_b, output, start_column, end_column))
    #         threads.append(thread)
    #         thread.start()
    
    #     self.__join__threads__(threads)
    #     return output

    def multiply_matrix_block(self, matrix_a, matrix_b, output, start_row, end_row, start_column, end_column):
        for i in range(start_row, end_row):
            for j in range(start_column, end_column):
                output[i, j] = 0
                for k in range(matrix_a.shape[1]):
                    output[i, j] += matrix_a[i, k] * matrix_b[k, j]

    
    def multiply_matrix_parallel(self, n_threads: int, matrix_a, matrix_b, output):
        n_rows, n_cols = matrix_a.shape[0], matrix_b.shape[1]
        n_threads = min(n_threads, n_rows * n_cols)
        
        block_size_row = max(1, n_rows // int(np.sqrt(n_threads)))
        block_size_col = max(1, n_cols // int(np.sqrt(n_threads)))
        
        threads = []
        for i in range(0, n_rows, block_size_row):
            for j in range(0, n_cols, block_size_col):
                end_row = min(i + block_size_row, n_rows)
                end_column = min(j + block_size_col, n_cols)
                
                thread = threading.Thread(target=self.multiply_matrix_block, args=(matrix_a, matrix_b, output, i, end_row, j, end_column))
                threads.append(thread)
                thread.start()
    
        self.__join__threads__(threads)
        return output
