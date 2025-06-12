##Dia 4 ejercicios de python...

import os

def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema

## 1
dias = ["Thirty", "Days", "Of","Python"]
resultado = " ".join(dias)
print(resultado)
## 1
pausa()
## 2
codigo = ["Coding","For","All"]
resultado = " ".join(codigo)
print(resultado)
## 2
pausa()

company = "Coding For All" # 3
print(company) # 4
print("La longitud de ",company," es: ",len(company)," caracteres")# 5
print("Transformando todos los caracteres de Coding For All a mayusculas: ",company.upper())## 6
print("Ahora se van a convertir todos los caracteres de Coding For All a minusculas: ",company.lower())## 7
pausa()
## 8
print("Variable capitalizada: ",company.capitalize())
print("Variable como título: ",company.title())
print("Variable con los caracteres invertidos: ",company.swapcase())
## 8
pausa()
## 9
print("Ahora vamos a quitar Coding de la variable: ",company.split(" ", 1)[1])
## 9
pausa()
## 10

## 10

