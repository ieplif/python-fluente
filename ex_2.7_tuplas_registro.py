# O significado depende da posição, não deve reordenar

# Latitude e longitude Aeroporto de Los Angeles

lax_coordinates= (33.9425, -118.408056)

# Dados sobre Tokyo
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

# Lista de tuplas ( código país e passaporte)

travels_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
               ('ESP', 'XDA205856')]

#  o operador % entende as tuplas e trata cada item como um campo separado
for passport in sorted(travels_ids):
    print('%s/%s' % passport)

# Laço for sabe obter itens da tupla separadamente, "desempacotamento",
# Não estamos interessados no segundo item, portanto usa-se _ captura valores q não queremos usar

for country, _ in travels_ids:
    print(country)

# Desempacotamento de tuplas - parallel assigment ( atribuição paralela)

latitude, longitude = lax_coordinates

latitude
longitude

# Desempacotamento prefixando um asterisco ao chamar a função

divmod(20, 8)

t = (20, 8)

divmod(*t)

quotient, remainder = divmod(*t)
quotient, remainder

# Função os.path.split() cria uma tupla (path, last_part) a partir de um caminho do sistema de arquivos

# _, filename = os.path.split('/home/filipe/idrsa.pub')
# filename -> idrsa.pub