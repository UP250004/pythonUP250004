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
pausa()
###### 3