# Cria uma lista de códigos Unicode(codepoints) a partir de uma String

symbols = '$¡§™¡§∞'

codes =[]

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)