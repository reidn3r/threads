from src.sum import MatrixSum
from src.multiply import MatrixMultiply
import numpy as np
import time

def main(sum:MatrixSum, multiply:MatrixMultiply, n_threads:int, matrix_a, matrix_b, output):
    p_start = time.time()
    sum.sum_matrix_parallel(n_threads, matrix_a, matrix_b, output)
    p_end = time.time()
    print(f'parallel sum: {p_end - p_start} s')

    seq_start = time.time()
    sum.sum_matrix_sequential(matrix_a, matrix_b, output)
    seq_end = time.time()
    print(f'sequential sum: {seq_end - seq_start} s\n')

    p_start = time.time()
    multiply.multiply_matrix_parallel(n_threads, matrix_a, matrix_b, output)
    p_end = time.time()
    print(f'parallel multiply: {p_end - p_start} s')
    
    seq_start = time.time()
    multiply.multiply_matrix_sequential(matrix_a, matrix_b, output)
    seq_end = time.time()
    print(f'sequential multiply: {seq_end - seq_start} s\n')

if __name__ == "__main__":
    np.random.seed(42)
    sum, mm = MatrixSum(), MatrixMultiply()

    n_threads:int = int(input("n threads: "))
    print("matriz: 100x100")
    matrix_a, matrix_b, output = sum.initialize_matrix(100)
    main(sum, mm, n_threads, matrix_a, matrix_b, output)

    print("matriz: 1000x1000")
    matrix_a, matrix_b, output = sum.initialize_matrix(1000)
    main(sum, mm, n_threads, matrix_a, matrix_b, output)
    