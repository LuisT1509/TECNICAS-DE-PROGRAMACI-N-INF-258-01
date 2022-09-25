# Escriba un programa que permita crear una lista de palabras y que, a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
# TAR04 - Luis Tavarez
# Matricula: 21-1673

# En esta parte el usuario podra ingresar las  palabras que se utilizaran para la lista de 4 palabras, para que pueda ingresar utilizamos input
numero1 = str(input("Escriba su primera palabra: "))
numero2 = str(input("Escriba su segunda palabra: "))
numero3 = str(input("Escriba su tercera palabra: "))
numero4 = str(input("Escriba su cuarta palabra: "))

# Aqui ya tendriamos la lista ya creada, utilizamos los corchetes para crearla y utilizamos append para que las variables ya completas salgan en forma de lista
# Despues  imprimimos la lista
lista = []
palabra1 = lista.append(numero1)
palabra2 = lista.append(numero2)
palabra3 = lista.append(numero3)
palabra4 = lista.append(numero4)
print("su lista ha sido creada:" + str(lista))

# En esta parte utilizamos las variables junto a: "for", "in", "if", "elif" y "else" para formular cada una de las funciones que se muestran a la hora de imprimirlo
palabra_repetida = str(input("Dígame la palabra a buscar: "))
contador = 0
for palabra in lista:          
  if palabra == palabra_repetida:
    contador += 1

# Imprimimos asegurandonos que las variables dentro del parentesis funcionen utilizando el signo de "+" para añadir esta misma.
# Dependiendo del numero que se repita una palabra saldra un mensaje relacionado, como podemos ver debajo.
if contador == 0:
          print("La palabra" + " ( " + palabra_repetida + " ) " "no aparece en la lista.")
          
elif contador == 1:
          print("La palabra" + " ( " + palabra_repetida + " ) " + "aparece una sola vez en la lista.")
else:
          print("La palabra" + " ( " + str(palabra_repetida) +  " ) "  "aparece en la lista"  +  " ( "  + str(contador) +  " ) "  "veces.")


