# TAR02 - Luis Tavarez
# Escribir un programa que pida 2 números y muestre paso a paso el cálculo de la raíz cuadrada de la suma del cuadrado de ambos. 
# Ingresamos los numeros que utilizaremos en la formula √a2+b2
from cmath import sqrt
import math
numero1 = input("Ingresar el primer numero= ")
numero2 = input("Ingresar el segundo numero= ")

# Verificamos que cada paso haga la funcion correcta
# Primer paso: se reemplaza la el numero por la variable
primerpaso = "√" + str(numero1) + "²"  "+" + str(numero2) + "²"

# Segundo paso: Se calculan los numeros elevedados
segundopaso = "√" + str(int(numero1)**2) + " + " + str(int(numero2)**2)

# Tercer paso: Se suman los numeros
tercerpaso = "√" + str(int(numero1)**2) + str(int(numero2)**2)

#Resultado: Se saca la raiz cuadrada
resultado = math.sqrt(int(numero1)**2 + int(numero2)**2)

# Imprimimos resultados
print(primerpaso)
print(segundopaso)
print(tercerpaso)
print(resultado)











