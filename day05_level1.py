####Dia 5
import os

def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema
## 1 Se declara una lista vacia...
listav = []
## 1
## 2
lista = ["Manzanas","Melones","Pepinos","Zanahorias","Naranjas", "Sandias"]
## 2
## 3 
print("Mi lista tiene lo siguiente: ",lista, " y la longitud de la misma es de: ",len(lista), " cosas")
## 3

## 4
print("Escogiendo la primer cosa de la lista, la del medio y la ultima, tengo las siguietes cosas: ")
print(lista[0]," ",lista[3]," ",lista[5])
## 4
pausa()

## 5
name,age,height,marital_status,address = "Brian",23,1.84,"Soltero","Benito Camelo #25"
mixed_data_types = [name,age,height,marital_status,address]
## 5

## 6
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
## 6
## 7
print("Lista de las compañias: \n",it_companies)
## 7
print("Numeros de las compañias (como estan acomodadas en la lista): ")
longitud= len(it_companies) + 1
face = longitud - len(it_companies)
goo = longitud - 5
mic = longitud - 4
app = longitud - 3
ib = longitud - 2
ora = longitud - 1
ama = longitud
num = [face,goo,mic,app,ib,ora,ama]
print(num)
## 8
print("")
## 8

## 9
print("Agarrando la compañia del inicio, medio y final de la lista: ")
print(lista[0]," ",lista[3]," ",lista[6])
## 9
pausa()
## 10
print(it_companies)
## 10