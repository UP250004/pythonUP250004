##### Dia 11
import os

def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema

###### Nivel 1
def sumar_dos_numeros(a, b):
    return a + b

def area_circulo(radio):
    from math import pi
    return pi * radio * radio

def sumar_todos(datos):
    if all(isinstance(i, (int, float)) for i in datos):
        return sum(datos)
    else:
        return "Todos los elementos deben ser números."

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def determinar_estacion(mes):
    mes = mes.lower()
    if mes in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif mes in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif mes in ['junio', 'julio', 'agosto']:
        return 'Verano'
    elif mes in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    else:
        return 'Mes no válido'

def calcular_pendiente(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def resolver_ecuacion_cuadratica(a, b, c):
    from math import sqrt
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales"
    x1 = (-b + sqrt(discriminante)) / (2*a)
    x2 = (-b - sqrt(discriminante)) / (2*a)
    return (x1, x2)

def imprimir_lista(lista):
    for item in lista:
        print(item)

def invertir_lista(lista):
    invertida = []
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    return invertida

def capitalizar_lista(lista):
    return [item.capitalize() for item in lista]

def agregar_elemento(lista, item):
    lista.append(item)
    return lista

def eliminar_elemento(lista, item):
    if item in lista:
        lista.remove(item)
    else: 
        print("Dato erroneo, no existe dicho elemento en la lista...")
    return lista

def suma_de_numeros(n):
    if all(isinstance(i, (int, float)) for i in datos):
        return sum(n)
    else:
        return "Todos los elementos deben ser números."
    

def suma_impares(n):
    if all(isinstance(i, (int, float)) for i in datos):
        return sum(i for i in n if i % 2 != 0)
    else:
        return "Todos los elementos deben ser números."

def suma_pares(n):
    if all(isinstance(i, (int, float)) for i in datos):
        return sum(i for i in n if i % 2 == 0)
    else:
        return "Todos los elementos deben ser números."
###### Nivel 1

###### Nivel 2
def pares_e_impares(n):
    pares = len([i for i in n if i % 2 == 0])
    impares = len([i for i in n if i % 2 != 0])
    print(f"El número de pares es {pares}.")
    print(f"El número de impares es {impares}.")

def factorial(n):
    from math import factorial
    return factorial(sum(n))

###### Nivel 2


#### Nivel 3
from data.countries_data import countries_data
from collections import Counter

def idiomas_mas_hablados(top=10):
    contador_idiomas = Counter()
    for pais in countries_data:
        for idioma in pais['languages']:
            contador_idiomas[idioma] += 1
    return contador_idiomas.most_common(top)

def paises_mas_poblados(top=10):
    poblados = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return [(pais['name'], pais['population']) for pais in poblados[:top]]
#### Nivel 3

#### Nivel 1

#### 1
print("Ejercicio 1, suma y resta por medio de una función definida...")
a = int(input("Dame un número: "))
b = int(input("Dame un número: "))
print("La suma de los 2 numeros fue de: ", sumar_dos_numeros(a,b))
#### 1
pausa()
#### 2
print("Ejercicio 2, área de un circulo...")
radio = int(input("Dame el radio de un circulo: "))
print("El area del circulo es de: ", area_circulo(radio))
#### 2
pausa()
#### 3
print("Ejercicio 3, suma de números...")
datos = [0]
cantidad = int(input("Dame la cantidad de numeros a sumar: "))
for i in range(cantidad):
    x = int(input(f"Dame el numero {i + 1} para agregarlo a la suma: "))
    datos.append(x)
print("La suma total de los numeros es de: ", sumar_todos(datos))
#### 3
pausa()
#### 4
print("Ejercicio 4, Celsius a Fahrenheit...")

calor = int(input("Dame los grados Celsius a convertir a Fahrenheit: "))
print(f"{calor} grados Celsius son {celsius_a_fahrenheit(calor)} grados Fahrenheit")
#### 4
pausa()

#### 5
print("Ejercicio 5, estación del año...")
mes = input("Dime un mes del año: ")
print(f"El mes {mes} pertenece a la estación {determinar_estacion(mes)}")
#### 5
pausa()

#### 6
print("Ejercicio 6, calculo de pendiente [(y2-y1) / (x2 - x1)]...")
x1 = int(input("Dame x1: "))
y1 = int(input("Dame y1: "))
x2 = int(input("Dame x2: "))
y2 = int(input("Dame y2: "))
print(f"La pendiente de las coordenadas ({x1},{y1}) y ({x2},{y2}) da como resultado: {calcular_pendiente(x1,y1,x2,y2)}")
#### 6
pausa()

#### 7
print("Ejercicio 7, ecuación cuadrática (ax^2 + bx + c = 0)...")
a = int(input("Dame a: "))
b = int(input("Dame b: "))
c = int(input("Dame c: "))
print(f"El resultado de la ecuacion es: {resolver_ecuacion_cuadratica(a,b,c)}")
#### 7
pausa()
#### 8
lista = []
cantidad = int(input("Dame la cantidad de objetos a considerar en la lista: "))
for i in range(cantidad):
    x = input(f"Dame el objeto {i + 1} para agregarlo a la lista: ")
    lista.append(x)
print("Los elementos de la lista: ", imprimir_lista(lista))
#### 8
pausa()
##### 9
print("A continuación se va a invertir la lista previa...")
print(invertir_lista(lista))
##### 9
pausa()
##### 10
print("A continuación se va a capitalizar los elementos de la lista previa...")
print(capitalizar_lista(lista))
##### 10
pausa()
##### 11
print("A continuación se va a capitalizar los elementos de la lista previa...")
print(capitalizar_lista(lista))
##### 11
pausa()
##### 12
item = input("Agrega un elemento a la lista: ")
print("La lista quedo como: ",agregar_elemento(lista,item))
##### 12
##### 13
item = input("Agrega un elemento a la lista: ")
print("La lista quedo como: ",agregar_elemento(lista,item))
##### 13
pausa()
#### 14
n = [0]
cantidad = int(input("Dame la cantidad de numeros a sumar: "))
for i in range(cantidad):
    x = int(input(f"Dame el numero {i + 1} para agregarlo a la suma: "))
    n.append(x)
print("Los numeros ingresados fueron: ",n)
print("La suma total de los numeros es de: ", suma_de_numeros(n))
#### 14
### 15
print(f"Suma de numeros impares:  {suma_impares(n)}")
### 15
### 16
print(f"Suma de numeros pares:  {suma_pares(n)}")
### 16
pausa()
#### Nivel 1

#### Nivel 2
#### 1
print(f"Se va a contar los numeros pares e impares de la lista: {n}")
print(pares_e_impares(n))
#### 1
#### 2
print(f"Se va a sacar el factorial de la lista {n}")
print(f"El factorial es: {factorial(n)}")
#### 2
pausa()
#### 4
#### Nivel 2

#### Nivel 3
print("Tomando en cuenta los datos de countries_data, se va a sacar los 10 idiomas más hablados en el mundo...")
print(idiomas_mas_hablados())
print("Tomando en cuenta los datos de countries_data, se va a sacar los 10 paises más poblados en el mundo...")
print(paises_mas_poblados())
#### Nivel 3