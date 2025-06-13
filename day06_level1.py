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
##### 1