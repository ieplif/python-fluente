
# Mecanismo de busca binária
# bisect encontra os pontos de inserçao para os itens em uma sequência ordenada
# haystack = palheiro, needle = agulha

import bisect
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d} {2}{0:<2d}'

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # Usa a função bisect escolhida para obter o ponto de interseção
        offset = position * '|'  # Cria um padrão de barras verticais proporcionais a offset
        print(ROW_FMT.format(needle, position, offset))  # Exibe as linhas formadas mostrando o valor de needle e o ponto de interseção

if __name__ == '__main__':
    if sys.argv[-1] == 'left': # Escolhe a função bisect a ser usada de acordo com o último argumento da linha de comando
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

print('DEMO:', bisect_fn.__name__)   # Exibe o cabeçalho com o nome da função selecionada
print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
demo(bisect_fn)