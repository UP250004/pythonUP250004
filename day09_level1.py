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

############# Ejercicios parte 1