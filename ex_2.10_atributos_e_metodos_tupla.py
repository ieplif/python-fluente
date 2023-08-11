# Atributos e métodos de uma tupla nomeada
# Continuação do exemplo 2.9

from collections import namedtuple

City = namedtuple('City', 'name country population coordinates')  # 2 parâmetros: nome de classe e lista dos nomes dos campos

tokyo = City('Tokyo', "JP", 36.933, (35.689722, 139.691667)) # dados passados como argumentos posicionais

City._fields  # _fields é uma tupla com os nomes dos campos da classe.

# ('name', 'country', 'population', 'coordinates')

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889))
delhi = City._make(delhi_data)  # -make permite instanciar uman tupla nomeda a partir a partir de um iterável (City(*delhi_data)) faria o mesmo
print(delhi._asdict())  # _asdict retorna uma collections.OrderedDict criado a partir da instância da tupola, exibe dados de forma legível

for key, value in delhi._asdict().items():
    print(key + ':', value)