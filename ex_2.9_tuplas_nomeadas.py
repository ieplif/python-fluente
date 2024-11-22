# Definindo e usando uma tupla nomeada

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')  # 2 parâmetros: nome de classe e lista dos nomes dos campos

tokyo = City('Tokyo', "JP", 36.933, (35.689722, 139.691667)) # dados passados como argumentos posicionais

print(tokyo)

print(tokyo.population)  # acessando os campos por nome ou posição

print(tokyo[1])
