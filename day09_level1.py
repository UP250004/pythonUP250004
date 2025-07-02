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
pausa()
############# Ejercicios parte 1

############# Ejercicios parte 2

################# 1
calif = int(input("Dame la calificacion de un estudiante de la UPA del 0-100: "))
if calif > 89 and calif < 101:
   print(f"El alumno saco la calificación aprobatoria de {calif}, A ")
elif calif > 69 and calif < 90:
   print(f"El alumno saco la calificación aprobatoria de {calif}, B ")
elif calif > 59 and calif < 70:
   print(f"El alumno saco la calificación reprobaprobatoria de {calif}, C ")
elif calif > 49 and calif < 60:
   print(f"El alumno saco la calificación reprobaprobatoria de {calif}, D ")
elif calif >= 0 and calif < 50:
   print(f"El alumno saco la calificación reprobaprobatoria de {calif}, F ")
################# 1

############# Ejercicios parte 2