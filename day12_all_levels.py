########### Dia 12
import os

def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema

import random
import string

# Función que genera un ID aleatorio de 6 caracteres
def generar_id_usuario():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choices(caracteres, k=6))

# Función que pide al usuario cantidad de caracteres y cantidad de IDs a generar
def generar_ids_por_usuario():
    longitud = int(input("Ingresa la longitud del ID: "))
    cantidad = int(input("Ingresa la cantidad de IDs a generar: "))
    caracteres = string.ascii_letters + string.digits
    for _ in range(cantidad):
        print(''.join(random.choices(caracteres, k=longitud)))

# Función que genera un color RGB aleatorio
def generar_color_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

# Ejemplo de uso:
# print(generar_id_usuario())
# generar_ids_por_usuario()
# print(generar_color_rgb())


# Función que genera una lista de colores en formato hexadecimal
def lista_de_colores_hexa(cantidad):
    colores = []
    for _ in range(cantidad):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colores.append(color)
    return colores

# Función que genera una lista de colores en formato RGB
def lista_de_colores_rgb(cantidad):
    return [generar_color_rgb() for _ in range(cantidad)]

# Función general para generar colores tipo 'hexa' o 'rgb'
def generar_colores(tipo, cantidad):
    if tipo == 'hexa':
        return lista_de_colores_hexa(cantidad)
    elif tipo == 'rgb':
        return lista_de_colores_rgb(cantidad)
    else:
        return "Tipo de color no válido. Usa 'hexa' o 'rgb'."

# Ejemplo:
# print(generar_colores('hexa', 3))
# print(generar_colores('rgb', 2))

# Función que desordena (baraja) una lista
def barajar_lista(lista):
    lista_barajada = lista[:]
    random.shuffle(lista_barajada)
    return lista_barajada

# Función que genera una lista de 7 números únicos aleatorios del 0 al 9
def siete_numeros_aleatorios_unicos():
    return random.sample(range(10), 7)

# Ejemplo:
# print(barajar_lista([1, 2, 3, 4, 5]))
# print(siete_numeros_aleatorios_unicos())


print("ID aleatorio:", generar_id_usuario())

print("\nGenerar múltiples IDs:")
generar_ids_por_usuario()

print("\nColor RGB aleatorio:", generar_color_rgb())

print("\nColores Hexa:", generar_colores('hexa', 3))
print("Colores RGB:", generar_colores('rgb', 3))

print("\nLista barajada:", barajar_lista([1, 2, 3, 4, 5]))
print("7 números únicos aleatorios:", siete_numeros_aleatorios_unicos())