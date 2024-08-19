# import threading
from utils.utils_matrix import Utils
from multiprocessing import Process
import time

class MatrixSum(Utils):
    def __init__(self) -> None:
        pass

    def sum_matrix_sequential(self, matrix_a, matrix_b, output, start_column=None, end_column=None, print_time=True):
        self.__check_matrix_dim__(matrix_a, matrix_b)
        
        start_column = 0 if start_column is None else start_column
        end_column = matrix_a.shape[1] if end_column is None else end_column
        
        start = time.time()
        for i in range(output.shape[0]):
            for j in range(start_column, end_column):
                output[i][j] = matrix_a[i][j] + matrix_b[i][j]
        end = time.time()

        if print_time:
            print(f'sequential sum: {end-start} s')

    def sum_matrix_parallel(self, n_threads:int, matrix_a, matrix_b, output):
        n_cols:int = matrix_a.shape[1]
        column_thread_ratio:int = n_cols // n_threads
        threads = []
        
        start = time.time()
        for i in range(n_threads):
            start_column:int = i * column_thread_ratio
            end_column:int = (i+1) * column_thread_ratio if i != n_threads - 1 else n_cols
            
            thread = Process(target=self.sum_matrix_sequential, args=(matrix_a, matrix_b, output, start_column, end_column, False))
            threads.append(thread)
            thread.start()

        end = time.time()
        print(f'parallel sum: {end-start} s')
        self.__join__threads__(threads)
        return output
