# TAR03 - Luis Tavarez
# Matricula: 21-1673 
# Escriba un programa que calcule el precio a pagar por el suministro de energía eléctrica. Se debe preguntar la cantidad de kwh consumidos y el tipo de instalación: R para residencias, I para industrias y C para comercios.

# Utilizamos un texto que indique que tiene que hacer el usuario, para esto usamos input

tipo_de_suministro = (input("¿Que tipo de suministro de energia usted ocupa? = "))
cantidad_KWH = int(input("ingresar kwh= "))

# Utilizamos if y elif como condiciones e imprimimos el resultado de "if" o "elif" para asi saber que opción saldrá dependiendo lo que haya escogido el usuario

if tipo_de_suministro == "R":

    if cantidad_KWH > 500:
          print("Su monto a pagar es RD$850.00")
    elif cantidad_KWH <= 500:
                print("Su monto a pagar es A RD550.00$")

if tipo_de_suministro == "I":
    if cantidad_KWH > 1000:
        print("Su monto a pagar es RD2500.00$")
    elif cantidad_KWH <= 1000:
                print("Su monto a pagar es RD1300.00$")

if tipo_de_suministro == "C":
    if cantidad_KWH > 5000:
        print("Su monto a pagar para es RD4200.00$")
    elif cantidad_KWH <= 5000:
             print("Su monto a pagar para es RD3800.00$")
