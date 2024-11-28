import time

def insertion_sort(arr):
    trocas = 0
    comparacoes = 0
    n = len(arr)
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        # Realiza comparações e trocas enquanto reorganiza os elementos
        while j >= 0:
            comparacoes += 1
            if arr[j] > chave:
                arr[j + 1] = arr[j]
                trocas += 1
                j -= 1
            else:
                break
        arr[j + 1] = chave
        if j + 1 != i:  # Conta como uma troca final quando o elemento é inserido
            trocas += 1
    return arr, trocas, comparacoes

# Função para abrir o arquivo e ler o vetor
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        vetor = [int(linha.strip()) for linha in file]
    return vetor

# Função principal
def main():
    nome_arquivo = r'C:\Users\artem\OneDrive\Área de Trabalho\-----\python\algoritmos de ordenação\nuemros para testes de paradigmas\100 mil numeros_decrescentes.txt'
    vetor = ler_arquivo(nome_arquivo)
    
    inicio_tempo = time.time()
    vetor_ordenado, trocas, comparacoes = insertion_sort(vetor)
    tempo_total = time.time() - inicio_tempo
    
    print("Vetor ordenado:", vetor_ordenado)
    print("Quantidade de trocas:", trocas)
    print("Quantidade de comparações:", comparacoes)
    print("Tempo necessário para ordenação:", tempo_total, "segundos")

# Executa o programa
main()
