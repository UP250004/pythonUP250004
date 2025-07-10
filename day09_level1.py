######## Dia 9

import os

def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema

############# Ejercicios parte 1

################# 1
edad = int(input("Dame tu edad: "))
if edad >= 18:
   print("Eres lo suficientemente grande para manejar y tener una licencia de conducir...")
elif edad < 18:
   print("No tienes edad suficiente para conducir")
else:
   print("Dato invalido...")
################# 1
pausa()
################# 2
mi_edad = 23
Edad = int(input("Dame tu edad: "))
if edad > mi_edad:
   resultado = edad - mi_edad
   print(f"Tu eres unos {resultado} años mayor a mi...")
elif edad < mi_edad:
   resultado = mi_edad - edad
   print(f"Tu eres unos {resultado} años menor a mi...")
elif edad == mi_edad:
   print(f"Tenemos la misma edad de {edad} años...")
else:
   print("Dato invalido...")
################# 2
pausa()
################# 3
a = int(input("Dame el numero 1: "))
b = int(input("Dame el numero 2: "))
if a > b:
   print(f"{a} es mayor a {b}")
elif a < b:
   print(f"{b} es mayor a {a}")
else:
   print("Datos invalido...")
################# 3
pausa()
############# Ejercicios parte 1

############# Ejercicios parte 2

################# 1
calif = int(input("Dame la calificacion de un estudiante de la UPA del 0-100: "))
if calif > 89 and calif < 101:
   print(f"El alumno saco la calificación aprobatoria de {calif}, A ")
elif calif > 69 and calif < 90:
   print(f"El alumno saco la calificación aprobatoria de {calif}, B ")
elif calif > 59 and calif < 70:
   print(f"El alumno saco la calificación reprobaprobatoria de {calif}, C ")
elif calif > 49 and calif < 60:
   print(f"El alumno saco la calificación reprobaprobatoria de {calif}, D ")
elif calif >= 0 and calif < 50:
   print(f"El alumno saco la calificación reprobaprobatoria de {calif}, F ")
################# 1
pausa()
############# Ejercicios parte 2
# 1. Determinar la estación del año según el mes
month = input("Ingresa el nombre de un mes (con la primera letra mayúscula): ")

if month in ['Septiembre', 'Octubre', 'Noviembre']:
    print("La estación es Otoño.")
elif month in ['Diciembre', 'Enero', 'Febrero']:
    print("La estación es Invierno.")
elif month in ['Marzo', 'Abril', 'Mayo']:
    print("La estación es Primavera.")
elif month in ['Junio', 'Julio', 'Agosto']:
    print("La estación es Verano.")
else:
    print("Mes no válido.")

print("\n---\n")
pausa()
# 2. Revisar o agregar frutas a la lista
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Ingresa el nombre de una fruta para revisar/agregar: ").lower()

if new_fruit in fruits:
    print("La fruta ya esta en la lista.")
else:
    fruits.append(new_fruit)
    print("Fruta agregada. Lista actualizada:", fruits)

print("\n---\n")
pausa()
# 3. Trabajar con el diccionario de persona
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Verificar si tiene clave 'skills' y mostrar habilidad del medio
if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Habilidad del medio:", skills[middle_index])

    # Verificar si sabe Python
    knows_python = 'Python' in skills
    print("¿Sabe Python?", knows_python)

    # Determinar tipo de desarrollador
    if set(skills) == {'JavaScript', 'React'}:
        print("He is a front end developer.")
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills):
        print("He is a backend developer.")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills):
        print("He is a fullstack developer.")
    else:
        print("Unknown title.")

# Verificar si está casado y vive en Finlandia
if person['is_marred'] and person['country'] == 'Finland':
    full_name = person['first_name'] + " " + person['last_name']
    print(f"{full_name} vive en Finlandia. El está casado.")
pausa()