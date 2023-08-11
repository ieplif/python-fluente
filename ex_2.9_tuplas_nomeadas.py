# Definindo e usando uma tupla nomeada

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')  # 2 parâmetros: nome de classe e lista dos nomes dos campos