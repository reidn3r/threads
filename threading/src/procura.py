import threading
import time

class MatrixSearch:
    def __init__(self):
        self.found = threading.Event()  # Evento para sinalizar que o elemento foi encontrado
        self.lock = threading.Lock()  # Lock para sincronização de threads

    def search_element_parallel(self, n_threads: int, matrix, element):
        '''
        - Função que procura um elemento na matriz utilizando múltiplas threads.
        '''
        # Start timing
        start_time = time.time()

        rows = matrix.shape[0]
        threads = []
        rows_per_thread = rows // n_threads

        for i in range(n_threads):
            start_row = i * rows_per_thread
            # A última thread pega as linhas restantes
            end_row = rows if i == n_threads - 1 else (i + 1) * rows_per_thread
            thread = threading.Thread(target=self.__search_in_rows__, args=(matrix, element, start_row, end_row))
            threads.append(thread)
            thread.start()

        # Aguardar todas as threads terminarem
        for thread in threads:
            thread.join()

        # End timing
        end_time = time.time()

        if not self.found.is_set():
            print(f"Elemento {element} não encontrado.")

        # Calculate elapsed time and print it
        elapsed_time = end_time - start_time
        print(f"Parallel search: {elapsed_time:.2f} seconds")

    def __search_in_rows__(self, matrix, element, start_row, end_row):
        for i in range(start_row, end_row):
            for j in range(matrix.shape[1]):
                if self.found.is_set():
                    return  # Se o elemento já foi encontrado, interrompe a busca
                if matrix[i, j] == element:
                    with self.lock:
                        if not self.found.is_set():
                            print(f"Elemento {element} encontrado na posição ({i}, {j})")
                            self.found.set()
                            return
