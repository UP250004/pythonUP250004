##### Dia 13
import os

def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema


# Ejercicios de comprensión de listas y funciones lambda en español

# 1. Filtrar solo números negativos y cero
numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_cero = [n for n in numeros if n <= 0]
print("Números negativos y ceros:", negativos_y_cero)
pausa()
# 2. Aplanar lista de listas de listas
listas_anidadas = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_aplanada = [num for sublist in listas_anidadas for inner in sublist for num in inner]
print("Lista aplanada:", lista_aplanada)
pausa()
# 3. Crear lista de tuplas con potencias
lista_tuplas = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print("Lista de tuplas:")
for t in lista_tuplas:
    print(t)
pausa()
# 4. Aplanar lista de países y transformar en lista con país, código, y ciudad en mayúsculas
paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
paises_formateados = [[pais.upper(), pais[:3].upper(), ciudad.upper()] for sublist in paises for (pais, ciudad) in sublist]
print("Lista formateada de países:", paises_formateados)
pausa()
# 5. Convertir lista de países en lista de diccionarios
paises_dicc = [{'country': pais.upper(), 'city': ciudad.upper()} for sublist in paises for (pais, ciudad) in sublist]
print("Lista de diccionarios de países:", paises_dicc)
pausa()
# 6. Convertir lista de nombres en lista de cadenas concatenadas
nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Barack', 'Obama')], [('Bill', 'Gates')]]
nombres_concatenados = [f"{nombre} {apellido}" for sublist in nombres for (nombre, apellido) in sublist]
print("Nombres concatenados:", nombres_concatenados)
pausa()
# 7. Función lambda para pendiente de una recta: pendiente = (y2 - y1) / (x2 - x1)
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
pausa()
# Ejemplo de uso de lambda
print("Pendiente entre (1, 2) y (3, 6):", pendiente(1, 2, 3, 6))
