import time
from collections import deque

def ler_labirinto(arquivo):
    try:
        with open(arquivo, 'r') as arquivo:
            labirinto = [list(line.strip()) for line in arquivo.readlines()]
        return labirinto
    except FileNotFoundError:
        print(f"Arquivo {arquivo} não encontrado.")
        return None

def bfs(labirinto, inicio, fim):
    queue = deque([inicio])
    veio_de = {inicio: None}
    
    while queue:
        atual = queue.popleft()
        if atual == fim:
            break
        
        for direcao in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            vizinho = (atual[0] + direcao[0], atual[1] + direcao[1])
            
            if (0 <= vizinho[0] < len(labirinto) and 0 <= vizinho[1] < len(labirinto[0]) and
                labirinto[atual[0]][atual[1]] != '#' and vizinho not in veio_de):
                queue.append(vizinho)
                veio_de[vizinho] = atual
    
    if fim not in veio_de:
        return None
    
    caminho = []
    passo = fim
    while passo is not None:
        caminho.append(passo)
        passo = veio_de[passo]
    caminho.reverse()
    return caminho

def find_inicio_fim(labirinto):
    inicio, fim = None, None
    for i, linha in enumerate(labirinto):
        for j, celula in enumerate(linha):
            if celula == 'S':
                inicio = (i, j)
            elif celula == 'E':
                fim = (i, j)
    return inicio, fim

def main():
    while True:
        arquivo = input("Informe o arquivo texto ou (0 para sair): ")
        if arquivo == '0':
            break
        
        labirinto = ler_labirinto(arquivo)
        if labirinto is None:
            continue

        inicio, fim = find_inicio_fim(labirinto)
        if not inicio or not fim:
            print("O labirinto deve conter 'S' e 'E' para início e fim.")
            continue

     
        print("BFS:")
        inicio_time = time.time()
        caminho = bfs(labirinto, inicio, fim)
        fim_time = time.time()

        if caminho:
            print(f"Caminho: {' '.join(map(str, caminho))}")
        else:
            print("Nenhum caminho encontrado.")
        print(f"Tempo: {fim_time - inicio_time:.3f} s")

if __name__ == "__main__":
    main()

