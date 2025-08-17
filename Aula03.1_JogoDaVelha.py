tabuleiro  = [
    ['','',''],
    ['','',''],
    ['','','']
]

jogador = "X"

def exibir_tabuleiro():
    for i, linha in enumerate(tabuleiro):
        print(' | '.join([c if c != '' else ' ' for c in linha]))
        if i < 2:
            print('-'*10)
       
def jogada(linha, coluna):
    global jogador
    if not 0 <= linha <= 2:
        print("Jogada inválida, tente novamente!")
        return jogador
    if not 0 <= coluna <= 2:
        print("Jogada inválida, tente novamente!")
        return jogador
    if tabuleiro[linha][coluna] != '':
        print("Jogada inválida, tente novamente!")
        return jogador 
    tabuleiro[linha][coluna] = jogador
    jogador = 'O' if jogador == 'X' else 'X'
    return jogador


def temGanhador():
    # Verifica as Linhas
    for linha in range(3):
        if (
            tabuleiro[linha][0] != '' and
            tabuleiro[linha][0] == tabuleiro[linha][1] and
            tabuleiro[linha][0] == tabuleiro[linha][2] 
        ):
            print(f"{tabuleiro[linha][0]} GANHOU!!")
            return True
    
    # Verifica as Colunas
    for coluna in range(3):
        if (
            tabuleiro[0][coluna] != '' and
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and
            tabuleiro[0][coluna] == tabuleiro[2][coluna]
        ):
            print(f"{tabuleiro[0][coluna]} GANHOU!!")
            return True

    # Verifica as Diagonais  
    if (
        tabuleiro[1][1] != '' and
        (
            (tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][2]) or
            (tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0])
        )
    ):
        print(f"{tabuleiro[1][1]} GANHOU!!")
        return True

    # Se não teve ganhador em nenhuma forma 
    return False

def temEmpate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == '':
                return False
    print("DEU VELHA!!")        
    return True        

def resetar_tabuleiro():
    global tabuleiro, jogador
    tabuleiro = [['','',''], ['','',''], ['','','']]
    jogador = "X"


# --- Loop principal ---
while True:
    print(f"Jogador da vez: {jogador}")
    try:
        linha = int(input("Digite a linha (0-2): "))
        coluna = int(input("Digite a coluna (0-2): "))
        jogada(linha, coluna)
    except IndexError:
        print("Digite valores entre 0 e 2")
    except ValueError:    
        print("Os valores devem ser números inteiros")  
    exibir_tabuleiro()
    
    if temGanhador() or temEmpate():
        opcao = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if opcao == "s":
            resetar_tabuleiro()
            continue
        else:
            print("Fim do jogo! Obrigado por jogar.")
            break
# Nosso tabuleiro é 3x3 e usa índices de 0 a 2:
""" Linha 0 -> primeira linha
Linha 1 -> segunda linha
Linha 2 -> terceira linha

Coluna 0 -> primeira coluna
Coluna 1 -> segunda coluna
Coluna 2 -> terceira coluna
"""