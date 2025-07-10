#####Dia 10
import os

def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema


######### Nivel 1

## 1
# Usando for
print("Usando el ciclo for...\n")
for i in range(11):
    print(i)
pausa()
# Usando while
print("Usando el ciclo while...\n")
i = 0
while i <= 10:
    print(i)
    i += 1
## 1
pausa()

## 2
# Usando for
print("Usando el ciclo for Else...\n")
for i in range(10, -1, -1):
    print(i)
else: 
    print("El ciclo de ha detenido en el numero: ", i)
pausa()
# Usando while
print("Usando el ciclo while...\n")
i = 10
while i >= 0:
    print(i)
    i -= 1
## 2
pausa()

############### 3
print("A continuacion se va a utilizar un ciclo for para imprimir un pino...")
for i in range(1, 8):
    print("#" * i)
############### 3
print("")
pausa()
############## 4
print("A continuacion se va a utilizar un ciclo for para imprimir un rectangulo...")
for i in range(8):
    print("\n")
    for j in range(8):
        print("#", end=" ")
############## 4
print("")
pausa()
############# 5
print("\nA continuacion se va a utilizar un ciclo for para imprimir una tabla de multiplicación de cuadrados...")
for i in range(11):
    print(f"{i} x {i} = {i * i}")
print("")
pausa()
############# 5

############# 6
techs = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in techs:
    print(tech)
print("")
pausa()
############# 6

############# 7
print("\nA continuacion se va a imprimir numeros pares del 0-100...")
for i in range(101):
    if i % 2 == 0:
        print(i)
print("")
pausa()
############# 7

############# 8
print("\nA continuacion se va a imprimir numeros impares del 0-100...")
for i in range(101):
    if i % 2 == 1:
        print(i)
print("")
pausa()
############# 8
######### Nivel 1