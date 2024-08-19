from utils.utils_matrix import Utils
from multiprocessing import Process
import time
# import threading

class MatrixMultiply(Utils):
    def __init__(self) -> None:
        pass

    def multiply_matrix_sequential(self, matrix_a, matrix_b, output):
        '''
            - Multiplica duas matrizes e retorna a matriz resultante.
                1. matrix_a, matrix_b: Matrizes de entrada
                2. output: Matriz resultante (matriz_a * matriz_b)
            
            - Faz uso do metodo privado __multiply_matrix_block__.
                - Nesse caso, o bloco a ser computado é a matriz toda
        '''
        start = time.time()
        output =  self.__multiply_matrix_block__(matrix_a, matrix_b, output, 0, matrix_a.shape[0], 0, matrix_a.shape[1])
        end = time.time()
        print(f'sequential multiply: {end-start} s\n')

    def multiply_matrix_parallel(self, n_threads: int, matrix_a, matrix_b, output):
        '''
            - Multiplicação de matrizes em paralelo:
                1. n_threads: Mínimo 1 thread para matriz toda, máximo 1 thread para cada elemento da matriz resultante
                2. b_size: Tamanho do bloco da matriz a ser computado
                    - Para cada bloco é criado uma thread responsável pela computação
                    - A computação de um determinado bloco é realizado pelo método privado __multiply_matrix_block__
        '''
        n_rows, n_cols = matrix_a.shape[0], matrix_b.shape[1]
    
        n_threads = min(n_threads, n_rows * n_cols)
        b_size = max(1, n_cols // n_threads) 

        start = time.time()
        threads = []
        for i in range(0, n_rows, b_size):
            for j in range(0, n_cols, b_size):
                end_row = min(i + b_size, n_rows)
                end_column = min(j + b_size, n_cols)
                
                thread = Process(target=self.__multiply_matrix_block__, args=(matrix_a, matrix_b, output, i, end_row, j, end_column))
                threads.append(thread)
                thread.start()

        self.__join__threads__(threads)

        end = time.time()
        print(f'parallel multiply: {end-start} s')

        return output
    
    def __multiply_matrix_block__(self, matrix_a, matrix_b, output, start_row, end_row, start_column, end_column):
        '''
            Processa região da matriz resultante, delimitado por:
                1. start_row, end_row: linhas iniciais e finais, respectivamente, da região a ser processada
                2. start_column, end_column: colunas iniciais e finais, respectivamente, da região a ser processada

            Segue o algoritmo tradicional de multiplicação de matrizes
            Complexidade: O(n^3)
        '''
        n_cols = matrix_a.shape[1]
        for i in range(start_row, end_row):
            for j in range(start_column, end_column):
                output[i, j] = 0
                for k in range(n_cols):
                    output[i, j] += matrix_a[i, k] * matrix_b[k, j]
