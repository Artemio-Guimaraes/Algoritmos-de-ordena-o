import time

def improved_bubble_sort(arr):
    n = len(arr)
    trocas = 0
    comparacoes = 0
    for i in range(n):
        # Otimização: flag para verificar se houve troca
        houve_troca = False
        for j in range(0, n - i - 1):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1
                houve_troca = True
        # Se não houve troca, o vetor já está ordenado
        if not houve_troca:
            break
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
    vetor_ordenado, trocas, comparacoes = improved_bubble_sort(vetor)
    tempo_total = time.time() - inicio_tempo
    
    print("Vetor ordenado:", vetor_ordenado)
    print("Quantidade de trocas:", trocas)
    print("Quantidade de comparações:", comparacoes)
    print("Tempo necessário para ordenação:", tempo_total, "segundos")

# Executa o programa
main()
