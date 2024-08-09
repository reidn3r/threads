from src.sum import MatrixSum
from src.multiply import MatrixMultiply

def main(sum:MatrixSum, multiply:MatrixMultiply, n_threads:int, matrix_a, matrix_b, output):
    sum.sum_matrix_parallel(n_threads, matrix_a, matrix_b, output)
    sum.sum_matrix_sequential(matrix_a, matrix_b, output, True)

    multiply.multiply_matrix_parallel(n_threads, matrix_a, matrix_b, output)    
    multiply.multiply_matrix_sequential(matrix_a, matrix_b, output)

if __name__ == "__main__":
    sizes = [100, 1000, 10_000, 100_000]
    sum, mm = MatrixSum(), MatrixMultiply()

    for size in sizes:
        print(f"matriz: {size}x{size}")
        n_threads:int = int(input("n threads: "))
        matrix_a, matrix_b, output = sum.initialize_matrix(size)
        main(sum, mm, n_threads, matrix_a, matrix_b, output)
    