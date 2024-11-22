# Cria uma lista de códigos Unicode(codepoints) a partir de uma String com list comprehensions

symbols = '$¡§™¡§∞'

codes =[ord(symbol) for symbol in symbols]

print(codes)