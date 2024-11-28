import time

# Função para ler o vetor do arquivo
def ler_vetor(arquivo):
    with open(arquivo, 'r') as f:
        vetor = [int(linha.strip()) for linha in f]
    return vetor

# Funções auxiliares para o heap sort
def heapify(arr, n, i, stats):
    maior = i       # Inicializa o maior como a raiz
    esq = 2 * i + 1 # Índice do filho à esquerda
    dir = 2 * i + 2 # Índice do filho à direita

    # Compara filho esquerdo
    if esq < n:
        stats["comparacoes"] += 1
        if arr[esq] > arr[maior]:
            maior = esq

    # Compara filho direito
    if dir < n:
        stats["comparacoes"] += 1
        if arr[dir] > arr[maior]:
            maior = dir

    # Se o maior não for a raiz
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]  # Troca
        stats["trocas"] += 1
        heapify(arr, n, maior, stats)

# Função principal do heap sort
def heap_sort(arr):
    n = len(arr)
    stats = {"comparacoes": 0, "trocas": 0} # Inicializa o contador de comparações e trocas

    # Constrói o heap (reorganiza o vetor)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, stats)

    # Extrai os elementos um a um do heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move a raiz atual para o final
        stats["trocas"] += 1
        heapify(arr, i, 0, stats)

    return stats

# Função principal
def main():
    # Lê o vetor do arquivo
    arquivo = r'C:\Users\artem\OneDrive\Área de Trabalho\-----\python\algoritmos de ordenação\nuemros para testes de paradigmas\10 mil numeros_aleatorios.txt'
    vetor = ler_vetor(arquivo)

    # Realiza o Heap Sort e mede o tempo
    inicio = time.time()
    stats = heap_sort(vetor)
    fim = time.time()
    tempo = fim - inicio

    # Exibe os resultados
    print("Vetor ordenado:", vetor)
    print("Tempo necessário:", tempo, "segundos")
    print("Quantidade de trocas:", stats["trocas"])
    print("Quantidade de comparações:", stats["comparacoes"])

# Chama a função principal
main()
