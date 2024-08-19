import numpy as np

class Utils:
    '''
        - Classe que fornece métodos para inicialização de 
        matrizes e gerenciamentos de threads.
    '''
    def __init__(self) -> None:
        pass

    def initialize_matrix(self, size:int):
        '''
            - Função que gera duas matrizes A e B de inteiros aleatórios e
            uma matriz de zeros, usada para receber a saída da operação
            entre A e B.
        '''
        matrix_a, matrix_b = self.__generate_random_matrix__(size), self.__generate_random_matrix__(size)
        output = np.zeros_like(matrix_a)
        return matrix_a, matrix_b, output
    
    def __check_matrix_dim__(self, matrix_a, matrix_b):
        '''
            - Método privado que verifica as dimensões de duas matrizes.
                1. Retorna True se forem de mesmas dimensões,
                caso contrário, gera interrupção
        '''
        if(matrix_a.shape != matrix_b.shape):
            raise AssertionError("sum: shapes should be equal.")
        return True
    
    def __join__threads__(self, threads:list):
        for t in threads:
            t.join()

    def __generate_random_matrix__(self, size:int):
        '''
            - Gera matriz quadrada de inteiros aleatórios, de tamanho size x size
                @size: Parâmetro que determina a dimensão da matriz quadrada 
        '''
        # low, high = -1024, 1024
        low, high = 0, 20
        return np.random.randint(size=size**2, low=low, high=high).reshape((-1, size))