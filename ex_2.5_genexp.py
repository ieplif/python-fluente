# Expressões geradoras - genexps

# Agora para criar sequências que não sejam listas (tuplas - diferentes tipos de dados, arrays - um tipo de dado, etc)

# Mesma sintaxe das listcomps mas são delimitadas por parênteses e não colchetes

# Genexps alimenta o laço for gerando um item de cada vez

import array

symbols = '$¢£#@¬'

tuple(ord(symbol) for symbol in symbols)

array.array('I', (ord(symbol) for symbol in symbols))