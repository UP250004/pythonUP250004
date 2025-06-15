####### Dia 6 --Tuples--
## Un "Tuple" son un conjunto de datos que son inmutables (o no cambiantes), se parece a una lista, con la diferencia que no se pueden modificar
##### Solo tienen pocos métodos 
# tuple(): to create an empty tuple
# count(): to count the number of a specified item in a tuple
# index(): to find the index of a specified item in a tuple
# operator: to join two or more tuples and to create a new 
import os
def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema

##### 1
print("Creando tuple vacio...")
Vacio = ()
##### 1
pausa()
##### 2
hermanas = ("Lety","Odette")
hermanos = ("Joaquin","Ryan")
print("Mis hermanas son: ",hermanas)
print("Mis hermanos son: ",hermanos)
##### 2
pausa()
##### 3
total_hermanos = hermanas + hermanos
print("Asi que tengo de hermanos a: ",total_hermanos)
##### 3
##### 4
print("Que son en total: ",len(total_hermanos))
##### 4
pausa()
##### 5
total_hermanos = total_hermanos[:2]
padres = ("Francelia","Ivan")
familia = total_hermanos + padres
print("Los miembros de mi familia son: ",familia)
##### 5

###### Ejercicios nivel 2...

##### 1
h_menor, h_media, mama, papa = familia
print("Mi hermana menor es: ",h_menor)
print("Mi hermana media es: ",h_media)
print("Mi mama es: ",mama)
print("Mi papa es: ",papa)
pausa()
##### 1

##### 2
frutas = ('platano', 'naranja', 'mango', 'limon', 'manzana')
verduras = ('lechuga', 'tomate', 'pepino', 'zanahoria', 'cebolla')
productos_animales = ('pollo', 'carne', 'pescado', 'huevo', 'queso')
print("Frutas: ", frutas)
print("Verduras: ", verduras)
print("Productos animales: ", productos_animales)
comida = frutas + verduras + productos_animales
print("Comida: ", comida)
##### 2
pausa()
##### 3
print("Ahora se va a convertir en lista el tuple comida...")
comida_lista = list(comida)
print("Comida como lista: ", comida_lista)
##### 3
pausa()
##### 4
def calculo_media(comida_lista):
    longitud = len(comida_lista)

    if longitud % 2 == 0:
        mitad1 = comida_lista[longitud // 2 - 1]
        mitad2 = comida_lista[longitud // 2]
        medio = (mitad1 + mitad2)
    else:
        medio = comida_lista[longitud// 2]
    return medio
media = calculo_media(comida_lista)
print("El valor medio de la lista comida es: ",media.capitalize())
##### 4

##### 5
print("Ahora vamos a poner los primeros 3 elementos y los últimos 3 elementos de la lista comida en un nuevo tuple...")
primeros_ultimos = tuple(comida_lista[:3] + comida_lista[-3:])
print("Los primeros 3 y los últimos 3 elementos de la lista comida son: ",primeros_ultimos)
###### 5
pausa()
##### 6
print("Ahora vamos a borrar la lista comida...")
del comida_lista
print("Lista comida borrada.")
##### 6
pausa()
##### 7
print("Ahora se va a comprobar si Estonia y/o Iceland están en el turple de países...")
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia está en los países nórdicos: ", 'Estonia' in nordic_countries)
print("Iceland está en los países nórdicos: ", 'Iceland' in nordic_countries)
##### 7
pausa()