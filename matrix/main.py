from src.sum import MatrixSum
import time

def main(sum:MatrixSum, n_threads:int, matrix_a, matrix_b, output):

    p_start = time.time()
    sum.sum_matrix_parallel(n_threads, matrix_a, matrix_b, output)
    p_end = time.time()
    print(f'parallel sum: {p_end - p_start} ms')


    seq_start = time.time()
    sum.sum_matrix_sequential(matrix_a, matrix_b, output)
    seq_end = time.time()
    print(f'sequential sum: {seq_end - seq_start} ms\n')
    return


if __name__ == "__main__":
    sum = MatrixSum()

    n_threads:int = int(input("soma - n threads: "))
    print("matriz: 100x100")
    matrix_a, matrix_b, output = sum.initialize_matrix(100)
    main(sum, n_threads, matrix_a, matrix_b, output)

    print("matriz: 1000x1000")
    matrix_a, matrix_b, output = sum.initialize_matrix(1000)
    main(sum, n_threads, matrix_a, matrix_b, output)
    