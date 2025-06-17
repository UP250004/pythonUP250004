#Dia 2 programando en Python (1-2)
# Variables en Python
import math
import os

first_name = 'Brian' #3
last_name = 'Rubio' #4
fullname = "Brian Odin Rubio Viramontes" #5
country = 'Mexico' #6
city = 'Aguascalientes' #7
age = 23 #8
year = 2002 #9
is_married = False #10
is_true = True #11
is_light_on = False #12
skills = ['HTML', 'CSS', 'Python', "C++"]#13
person_info = {
    'firstname':first_name, 
    'lastname':last_name, 
    'country':country,
    'city':city
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Brian', 'Rubio', "Mexico", 23, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)


#####################
print(type(first_name))   # String
print(type(last_name)) # String
print(type(country))    # String
print(type(person_info))    # Dict
#####################

#####################
print(len(first_name)) 
print(len(last_name)) 
print(len(country)) 
print(len(first_name)) 
#####################
print("Presiona enter para continuar...")
input("")  # Pausa la ejecución hasta que el usuario presione Enter
os.system("cls")#Limpia la pantalla del sistema
##################### Ejercicios nivel 2.
number_one, number_two = 5,4
total= number_one + number_two
diff = number_one - number_two
product = number_two * number_one
division = number_one / number_two
remainder = number_one % number_two
exp = number_one ** number_two
floor_division = number_one // number_two
print("La suma de ", number_one, " y ", number_two, "es: ", total)
print("La resta de ", number_one, " y ", number_two, "es: ", diff)
print("La multiplicación de ", number_one, " y ", number_two, "es: ", product)
print("La división de ", number_one, " y ", number_two, "es: ", round(division,2))
print("El residuo de la división de ", number_one, " y ", number_two, "es: ", remainder)
print("La potencia del numero ", number_one, " elevado a ", number_two, "es: ", exp)
print("La floor division de ", number_one, " y ", number_two, "es: ", floor_division)

print("Presiona enter para continuar...")
input("")  # Pausa la ejecución hasta que el usuario presione Enter
os.system("cls")#Limpia la pantalla del sistema

print("A continuacion se va a calcular el area y la circuferencia de un circulo de radio de 30 metros")
radio = 30
Area = math.pi*(radio*radio)
Circu = math.pi*(radio*2)
print("El area del circulo es de ", round(Area,2), " metros, mientras que su circunferencia es de ", round(Circu,2), " metros")

print("Presiona enter para continuar...")
input("")  # Pausa la ejecución hasta que el usuario presione Enter
os.system("cls")#Limpia la pantalla del sistema

print("Ahora es tu turno de determinar el area del circulo con un radio que me proporciones ...")
radio_2 = int(input("Dame el radio del circulo: "))
Area_2 = math.pi*(radio_2*radio_2)
Circu_2 = math.pi*(radio_2*2)
print("El area del circulo en base al radio puesto es de ", round(Area_2,2), " metros, mientras que su circunferencia es de ", round(Circu_2,2), " metros")

print("Presiona enter para continuar...")
input("")  # Pausa la ejecución hasta que el usuario presione Enter
os.system("cls")#Limpia la pantalla del sistema

firstname = input("Dame tu primer nombre: ")
lastname = input("Dame tu apellido: ")
country = input("Dame tu pais de origen: ")
print("Eres ", firstname, " ", lastname, ", ", "eres del pais de ", country)
##################### Ejercicios nivel 2.