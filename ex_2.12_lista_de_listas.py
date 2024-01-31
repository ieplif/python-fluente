
# Uma lista com três listas detamanho 3 pode ser representar um tabuleiro de jogo da velha


# utilizando list comprehension
board = [['_'] * 3 for i in range(3)]  # Cria uma lista de três listas com três itens cada
print(board)

board[1][2] = 'X'  # Coloca uma marca na linha 1 coluna 2

print(board)


# código equivalente

board = []
for i in range(3):
    row = ['_'] * 3  #  cada iteração cra um novo row e concatena a board
    board.append(row)

print(board)

board[2][0] = 'O'

print(board)