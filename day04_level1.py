##Dia 4 ejercicios de python...

import os

def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema

## 1
dias = ["Thirty", "Days", "Of","Python"]
py= "Python for Everyone"
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
print("Se va a verificar en que parte de la variable se encuentra Coding ",company.index("Coding"))
## 10
pausa()
## 11
print("Ahora se va a reemplazar Coding por la palabra Python: ",company.replace("Coding","Python"))
## 11
pausa()
## 12
print("Se va a sustituir la palabra Everyone por All en la variable py: ",py.replace("Everyone","All"))
## 12
pausa()
## 13
print("Se va a separar la variable company por medio de la funcion split(): ",company.split(" "))
## 13
pausa()
## 14
Compañias = "Facebook, Google, Microsoft, Apple,IBM, Oracle, Amazon"
print("Ahora se va a separar por espacios entre las comas (,) las siguientes compañias: ",Compañias.split(", "))
## 14
pausa()
## 15
print("El caracter 0 es C en este caso: ",company.index("C"))
## 15
pausa()
## 16
print("El caracter final ",company.index("l")," es l en Coding For All")
## 16
pausa()
## 17
print("El caracter ",company.index(" A")," es un espacio en blanco antes de la A en Coding For All")
## 17
pausa()
## 18
pfe= "Python for Everyone"
## 18

## 19
cfa = "Coding For All"
## 19
pausa()
## 20
print("C se encuentra en la posicion:",cfa.index("C"),"dentro de ", cfa)
## 20

## 21
print("F se encuentra en la posicion:",cfa.index("F"),"dentro de ", cfa)
## 21

## 22
print("l se encuentra en la posicion:",cfa.rfind("l"),"dentro de ", cfa)
## 22
pausa()
## 23
palabra = "You cannot end a sentence with because because because is a conjunction"
print("because se puede encontrar primero en la posicion:",palabra.index("because"),"dentro de ", palabra)
## 23

## 24
print("because se puede encontrar al final en la posicion:",palabra.rindex("because"),"dentro de ", palabra)
## 24

## 25
salto1 = palabra[0:31]
salto2 = palabra[54:]
print(salto1+salto2) ##31-54
## 25
pausa()
## 26
print("because se puede encontrar primero en la posicion:",palabra.index("because"),"dentro de ", palabra)
## 26
pausa()
## 27
salto1 = palabra[0:31]
salto2 = palabra[54:]
print(salto1+salto2) ##31-54
## 27

## 28-29
print("Coding si se encuentra:",cfa.find("Coding"),", dentro de ", cfa," por que dio 0, lo que significa found....")
print("coding no se encuentra:",cfa.rfind("coding"),", dentro de ", cfa," por que dio -1, lo que significa not found...")
## 28-29
pausa()
## 30
pal = " Coding For All    "
print("Quitando los espacios de \"",pal,"\"")
pal = pal.strip()
print(pal,".")
## 30
pausa()
reto = '30DaysOfPython'
reto2 = 'thirty_days_of_python'
print("Se va a usar una variable para verificar si los nombres son correctos:")
print(reto)
print(reto.isidentifier(), " por que no es un nombre valido") # Falso
print(reto2)
print(reto2.isidentifier()," por que es un nombre valido") # True
## 31
pausa()
## 32
lista = ["Coding","For","All"]
resultado = " ".join(lista)
print(resultado)
## 32