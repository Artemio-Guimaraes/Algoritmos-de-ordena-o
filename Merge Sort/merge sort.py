import time

# Contadores globais para trocas e comparações
comparacoes = 0
fusoes = 0  # Usando "fusões" como aproximação para trocas

def merge_sort(arr):
    global comparacoes, fusoes
    
    # Caso base: vetor com apenas um elemento
    if len(arr) <= 1:
        return arr
    
    # Divisão do vetor
    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])
    
    # Fusão das duas metades
    return merge(esquerda, direita)

def merge(esquerda, direita):
    global comparacoes, fusoes
    resultado = []
    i = j = 0

    # Comparação e fusão dos elementos
    while i < len(esquerda) and j < len(direita):
        comparacoes += 1
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
        fusoes += 1  # Cada adição ao vetor resultado conta como uma fusão

    # Adiciona os elementos restantes de cada metade (sem comparação)
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    fusoes += len(esquerda[i:]) + len(direita[j:])

    return resultado

# Função para abrir o arquivo e ler o vetor
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        vetor = [int(linha.strip()) for linha in file]
    return vetor

# Função principal
def main():
    global comparacoes, fusoes
    nome_arquivo = r'C:\Users\artem\OneDrive\Área de Trabalho\-----\python\algoritmos de ordenação\nuemros para testes de paradigmas\100 mil numeros_decrescentes.txt'
    vetor = ler_arquivo(nome_arquivo)
    
    inicio_tempo = time.time()
    vetor_ordenado = merge_sort(vetor)
    tempo_total = time.time() - inicio_tempo
    
    print("Vetor ordenado:", vetor_ordenado)
    print("Quantidade de fusões (como trocas):", fusoes)
    print("Quantidade de comparações:", comparacoes)
    print("Tempo necessário para ordenação:", tempo_total, "segundos")

# Executa o programa
main()
