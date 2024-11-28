import time

def bubble_sort(arr):
    n = len(arr)
    trocas = 0
    comparacoes = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparacoes += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1
    return arr, trocas, comparacoes

# Abrindo o arquivo e lendo o vetor
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        vetor = [int(linha.strip()) for linha in file]
    return vetor

# Função principal
def main():
    nome_arquivo = r'C:\Users\artem\OneDrive\Área de Trabalho\-----\python\algoritmos de ordenação\nuemros para testes de paradigmas\100 mil numeros_decrescentes.txt'
    vetor = ler_arquivo(nome_arquivo)
    
    inicio_tempo = time.time()
    vetor_ordenado, trocas, comparacoes = bubble_sort(vetor)
    tempo_total = time.time() - inicio_tempo
    
    print("Vetor ordenado:", vetor_ordenado)
    print("Quantidade de trocas:", trocas)
    print("Quantidade de comparações:", comparacoes)
    print("Tempo necessário para ordenação:", tempo_total, "segundos")

# Executa o programa
main()
