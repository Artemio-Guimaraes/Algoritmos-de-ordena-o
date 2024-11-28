import time

def selection_sort(arr):
    n = len(arr)
    trocas = 0
    comparacoes = 0
    for i in range(n):
        # Assume que o primeiro elemento não ordenado é o menor
        min_index = i
        for j in range(i + 1, n):
            comparacoes += 1
            if arr[j] < arr[min_index]:
                min_index = j
        # Realiza a troca se o índice do menor elemento mudou
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            trocas += 1
    return arr, trocas, comparacoes

# Função para abrir o arquivo e ler o vetor
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        vetor = [int(linha.strip()) for linha in file]
    return vetor

# Função principal
def main():
    nome_arquivo = r'C:\Users\artem\OneDrive\Área de Trabalho\-----\python\algoritmos de ordenação\nuemros para testes de paradigmas\mil numeros_aleatorios.txt'
    vetor = ler_arquivo(nome_arquivo)
    
    inicio_tempo = time.time()
    vetor_ordenado, trocas, comparacoes = selection_sort(vetor)
    tempo_total = time.time() - inicio_tempo
    
    print("Vetor ordenado:", vetor_ordenado)
    print("Quantidade de trocas:", trocas)
    print("Quantidade de comparações:", comparacoes)
    print("Tempo necessário para ordenação:", tempo_total, "segundos")

# Executa o programa
main()