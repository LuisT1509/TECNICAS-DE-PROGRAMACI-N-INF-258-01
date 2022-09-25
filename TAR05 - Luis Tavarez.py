# Escriba un programa que pregunte al usuario los números de su ticket de lotería, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 
# TAR05 - Luis Tavarez
# Matricula: 21-1673

from csv import list_dialects

# Creamos la lista utilizando los corchetes.
lista = [] 

# Ponemos que para numero_loteria ponga 6 veces el texto de abajo, usamos el input para que el usuario pueda ingresar los numeros.
for numero_loteria in range(6):
    lista.append(int(input("Ingrese el numero de loteria= ")))

# Utilizamos sort para poder ordenar los numeros de menor a mayor o en el orden ascendiendo e imprimos la lista.