import time
import random

# Classe para monitorar comparações e trocas
class QuickSortStats:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0

    def increment_comparisons(self):
        self.comparisons += 1

    def increment_swaps(self):
        self.swaps += 1

# Função para trocar elementos
def swap(arr, i, j, stats):
    arr[i], arr[j] = arr[j], arr[i]
    stats.increment_swaps()

# Função para escolher um pivô aleatório
def choose_random_pivot(low, high):
    return random.randint(low, high)

# Função para particionar o array
def partition(arr, low, high, stats):
    # Escolha um pivô aleatório e mova-o para o final
    pivot_index = choose_random_pivot(low, high)
    swap(arr, pivot_index, high, stats)
    pivot = arr[high]

    i = low - 1
    for j in range(low, high):
        stats.increment_comparisons()
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j, stats)

    # Coloque o pivô na posição correta
    swap(arr, i + 1, high, stats)
    return i + 1

# Implementação iterativa do QuickSort
def quick_sort_iterative(arr, stats):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(arr, low, high, stats)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

# Função para carregar números de um arquivo
def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return [int(line.strip()) for line in file if line.strip()]
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []

# Função principal
def main():
    filename = r"C:\Users\artem\OneDrive\Área de Trabalho\-----\python\algoritmos de ordenação\nuemros para testes de paradigmas\mil numeros_ordenados.txt"  # Substitua pelo nome do arquivo
    arr = read_numbers_from_file(filename)
    if not arr:
        print("Nenhum número foi carregado do arquivo.")
        return

    stats = QuickSortStats()

    start_time = time.perf_counter()
    quick_sort_iterative(arr, stats)
    end_time = time.perf_counter()

    print("Vetor ordenado:", arr)
    print(f"Total de comparações: {stats.comparisons:,}")
    print(f"Total de trocas: {stats.swaps:,}")
    print(f"Tempo gasto: {end_time - start_time:.6f} segundos")

if __name__ == "__main__":
    main()