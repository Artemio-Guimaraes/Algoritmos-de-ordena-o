import time

# Função para realizar a ordenação usando Tim Sort
def tim_sort(arr):
    min_run = 32
    n = len(arr)
    comparisons = 0
    swaps = 0

    # Função para inserir elementos em uma sublista
    def insertion_sort(sub_arr, left, right):
        nonlocal comparisons, swaps
        for i in range(left + 1, right + 1):
            key_item = sub_arr[i]
            j = i - 1
            while j >= left and sub_arr[j] > key_item:
                comparisons += 1
                sub_arr[j + 1] = sub_arr[j]
                swaps += 1
                j -= 1
            sub_arr[j + 1] = key_item
            if j >= left:
                comparisons += 1

    # Função para mesclar sublistas
    def merge(left, mid, right):
        nonlocal comparisons, swaps
        left_copy = arr[left:mid + 1]
        right_copy = arr[mid + 1:right + 1]
        i = 0
        j = 0
        k = left

        while i < len(left_copy) and j < len(right_copy):
            comparisons += 1
            if left_copy[i] <= right_copy[j]:
                arr[k] = left_copy[i]
                i += 1
            else:
                arr[k] = right_copy[j]
                j += 1
            swaps += 1
            k += 1

        while i < len(left_copy):
            arr[k] = left_copy[i]
            i += 1
            k += 1
            swaps += 1

        while j < len(right_copy):
            arr[k] = right_copy[j]
            j += 1
            k += 1
            swaps += 1

    # Ordenação por inserção para sublistas
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    # Mesclando as sublistas
    size = min_run
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(left, mid, right)
        size *= 2

    return comparisons, swaps

# Função para ler o vetor do arquivo
def ler_vetor_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        return [int(line.strip()) for line in file]

# Caminho do arquivo
nome_arquivo = r'C:\Users\artem\OneDrive\Área de Trabalho\-----\python\algoritmos de ordenação\nuemros para testes de paradigmas\100 mil numeros_aleatorios.txt'

# Lendo o vetor do arquivo
vetor = ler_vetor_do_arquivo(nome_arquivo)

# Medindo o tempo de execução
inicio = time.time()
comparacoes, trocas = tim_sort(vetor)
tempo_execucao = time.time() - inicio

# Resultados
print(f"Quantidade de comparações: {comparacoes}")
print(f"Quantidade de trocas: {trocas}")
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")