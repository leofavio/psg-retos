texto=input()
cantPalabras=len(texto.split())
print("Cantidad de palabras:",cantPalabras)

vocal=texto.lower().count('a')+texto.lower().count('e')+texto.lower().count('i')+texto.lower().count('o')+texto.lower().count('u')
print("Cantidad de vocales:",vocal)

sinEspacios=texto.replace(" ","").lower()

alReves="".join(reversed(sinEspacios))

print("Es palíndromo:",sinEspacios==alReves)