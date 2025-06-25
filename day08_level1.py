##### Dia 8
import os

def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema

# 1. Crear un diccionario vacío llamado 'dog'
dog = {}

# 2. Agregar name, color, breed, legs, age al diccionario dog
dog["name"] = "Fido"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 5

print("Dog dictionary:", dog)
pausa()
# 3. Crear un diccionario de estudiante con varias claves
student = {
    "first_name": "Ana",
    "last_name": "García",
    "gender": "Female",
    "age": 21,
    "marital_status": "Single",
    "skills": ["Python", "HTML"],
    "country": "Mexico",
    "city": "Guadalajara",
    "address": "Calle Falsa 123"
}

# 4. Obtener la longitud del diccionario student
print("Longitud del diccionario del estudiante:", len(student))
pausa()
# 5. Obtener el valor de 'skills' y comprobar su tipo
skills = student["skills"]
print("Skills:", skills)
print("Type of skills:", type(skills))
pausa()
# 6. Modificar 'skills' agregando una o dos habilidades
student["skills"].append("CSS")
student["skills"].extend(["JavaScript"])
print("Updated skills:", student["skills"])
pausa()
# 7. Obtener las claves del diccionario como lista
keys = list(student.keys())
print("Dictionary keys:", keys)
pausa()
# 8. Obtener los valores del diccionario como lista
values = list(student.values())
print("Dictionary values:", values)
pausa()
# 9. Convertir el diccionario a una lista de tuplas con items()
items = list(student.items())
print("Dictionary as list of tuples:", items)
pausa()
# 10. Eliminar uno de los elementos del diccionario
del student["marital_status"]
print("After deleting 'marital_status':", student)
pausa()
# 11. Eliminar el diccionario completo
del dog
# print(dog)  # Esto causaría un error si se descomenta: NameError: name 'dog' is not defined