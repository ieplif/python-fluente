
# Com referência à mesma lista é inútil

# Com list comprehension
weird_board = [['_'] * 3] * 3  # três referências à mesma lista interna

print(weird_board)

weird_board[1][2] = 'O'

print(weird_board)  # todas as linhas são aliases que se referem ao mesmo objeto, marca 3x

# código equivalente

row = ['_'] * 3
board = []

for i in range(3):
    board.append(row)