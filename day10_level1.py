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
    ## otra forma de hacerlo: if i % 2 != 0:
    if i % 2 == 1:
        print(i)
print("")
pausa()
############# 8
######### Nivel 1

######### Nivel 2
############# 1
x = 0 
print("\nA continuacion se va a imprimir numeros del 0-100...")
for i in range(101):
    x = i + x
    print(i)
print("")
print(f"La suma de los numeros es: {x}")
pausa()
############# 1

############# 2
x = 0
y = 0
print("\nA continuacion se va a imprimir numeros impares del 0-100...")
for i in range(101):
    ## otra forma de hacerlo: if i % 2 != 0:
    if i % 2 == 1:
        print(i)
        x = x + i
    elif i % 2 == 0:
        y = y + i
print("")
print(f"La suma de los numeros impares es: {x}")
print(f"La suma de los numeros pares es: {y}")
pausa()

######### Nivel 2


######### Nivel 3
from data.countries import countries
from data.countries_data import countries_data

# 1. Extraer países que contienen "land"
land_countries = [country for country in countries if 'land' in country]
print("Países que contienen 'land':", land_countries)

# 2. Invertir una lista de frutas usando un bucle
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i])
print("Frutas en orden inverso:", reversed_fruits)

# 3. Total de idiomas únicos
unique_languages = set()
for country in countries_data:
    for language in country['languages']:
        unique_languages.add(language)

print("Total de idiomas únicos:", len(unique_languages))

# 4. Diez idiomas más hablados
from collections import Counter

language_counter = Counter()
for country in countries_data:
    for lang in country['languages']:
        language_counter[lang] += 1

most_spoken = language_counter.most_common(10)
print("10 idiomas más hablados:")
for lang, count in most_spoken:
    print(f"{lang}: {count} países")

# 5. 10 países más poblados
sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
top_10_populated = sorted_countries[:10]

print("\n10 países más poblados:")
for country in top_10_populated:
    print(f"{country['name']}: {country['population']:,} habitantes")

######### Nivel 3