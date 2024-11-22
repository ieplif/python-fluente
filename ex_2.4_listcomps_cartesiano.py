# Gera uma lista de tuplas organizadas, por cor e , em seguida, por tamanho

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]

print(tshirts)

# loops aninhados aparece na mesma ordem q a anterior
for color in colors:
    for size in sizes:
        print((color, size))


# Adicionando quebra de linha organiza por tamanho e cor
tshirts = [(color, size) for size in sizes
                         for color in colors]

print(tshirts)