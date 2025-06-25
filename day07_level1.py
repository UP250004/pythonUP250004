#### Dia 7
import os
def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#### Ejercicios nivel 1
####### 1
print("La longitud del set \"it_companies\" es: ",len(it_companies))
pausa()
####### 1

###### 2
print("Se va a agregar a \"Twitter\" en las compañias: ")
t= {"Twitter"}
it_companies = it_companies.union(t)
print(it_companies)
###### 2
pausa()
###### 3
print("Ahora se va a agregar a más compañias: ")
t= {"Bad Dragon","NVIDIA","Intel","AMD","HP"}
it_companies = it_companies.union(t)
print(it_companies)
###### 3
pausa()
###### 4
print("Ahora se va a quitar una compañia: ")
it_companies.remove("Bad Dragon")
print(it_companies)
###### 4

###### 5
#remove(element)
#Elimina el element del set.

#Lanza un error (KeyError) si el element no está presente en el set.
# = {1, 2, 3}
#s.remove(2)  # OK
#s.remove(5)  # ❌ KeyError: 5 not found

#discard(element)
#Elimina el element del set.
#No lanza error si el element no está presente.
#s = {1, 2, 3}
#s.discard(2)  # OK
#s.discard(5)  # OK, no hace nada
###### 5

#### Ejercicios nivel 1