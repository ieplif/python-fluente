colors = ['black', 'white']
sizes = ['S', 'M', 'L']


# gera itens um por um, não construirá uma lista

for tshirt in (f'{c} {s}' for c in colors for s in sizes):
    print(tshirt)

