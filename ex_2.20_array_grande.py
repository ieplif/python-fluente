# Criando, salvando e carregando um array com 10 milhões de númeors ponto flutuante aleatórios

from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))

print(floats[-1])

fp = open('floats.bin', 'wb')
floats.tofile(fp)  # Salva o array em um arquivo binário

fp.close()

floats2 = array('d')

fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)  # Lê 10 milhões de números no arquivo binário
fp.close()

print(floats2[-1])

print(floats2 == floats)  # Verifica se o conteúdo dos arryas coincide