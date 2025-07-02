######## Dia 9

import os

def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema

############# Ejercicios parte 1

################# 1
edad = int(input("Dame tu edad: "))
if edad >= 18:
   print("Eres lo suficientemente grande para manejar y tener una licencia de conducir...")
elif edad < 18:
   print("No tienes edad suficiente para conducir")
else:
   print("Dato invalido...")
################# 1
pausa()
################# 2
mi_edad = 23
Edad = int(input("Dame tu edad: "))
if edad > mi_edad:
   resultado = edad - mi_edad
   print(f"Tu eres unos {resultado} años mayor a mi...")
elif edad < mi_edad:
   resultado = mi_edad - edad
   print(f"Tu eres unos {resultado} años menor a mi...")
elif edad == mi_edad:
   print(f"Tenemos la misma edad de {edad} años...")
else:
   print("Dato invalido...")
################# 2
pausa()
################# 3
a = int(input("Dame el numero 1: "))
b = int(input("Dame el numero 2: "))
if a > b:
   print(f"{a} es mayor a {b}")
elif a < b:
   print(f"{b} es mayor a {a}")
else:
   print("Datos invalido...")
################# 3

############# Ejercicios parte 1