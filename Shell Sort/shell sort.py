import time

def shell_sort(arr):
    n = len(arr)
    trocas = 0
    comparacoes = 0
    gap = n // 2  # Inicializa o intervalo (gap)

    # Executa o Shell Sort com intervalos decrescentes
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Ordena os elementos com o intervalo atual
            while j >= gap:
                comparacoes += 1
                if arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                    trocas += 1
                else:
                    break

            # Insere o elemento temporário na posição correta
            arr[j] = temp
            if j != i:
                trocas += 1  # Conta a troca final para posicionar o elemento

        gap //= 2  # Reduz o intervalo

    return arr, trocas, comparacoes

# Função para abrir o arquivo e ler o vetor
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        vetor = [int(linha.strip()) for linha in file]
    return vetor

# Função principal
def main():
    nome_arquivo = r'C:\Users\artem\OneDrive\Área de Trabalho\-----\python\algoritmos de ordenação\nuemros para testes de paradigmas\mil numeros_decrescentes.txt'
    vetor = ler_arquivo(nome_arquivo)
    
    inicio_tempo = time.time()
    vetor_ordenado, trocas, comparacoes = shell_sort(vetor)
    tempo_total = time.time() - inicio_tempo
    
    print("Vetor ordenado:", vetor_ordenado)
    print("Quantidade de trocas:", trocas)
    print("Quantidade de comparações:", comparacoes)
    print("Tempo necessário para ordenação:", tempo_total, "segundos")

# Executa o programa
main()
