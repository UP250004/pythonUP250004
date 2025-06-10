import math
import os

def pausa():
   print("Presiona enter para continuar...")
   input("")  # Pausa la ejecución hasta que el usuario presione Enter
   os.system("cls")#Limpia la pantalla del sistema

########Datos personales
edad = 23
estatura = 1.84
compleja = 69 + 420j
########Datos personales
###############################Triángulo
print("A continuacion vas a introducir la base y la altura de un triangulo para poder calcular su área la cual va a ser considerada en metros...")
base = int(input("Dame la base del triangulo: "))
altura = int(input("Dame la altura del triangulo: "))
area = (base*altura)/2
print("Con los datos proporcionados, la área del triangulo es de ", area, " metros.")
print("Bien hecho!!!, ahora toca calcular el perimetro del triangulo con las medidas que me proporciones...")
a=int(input("Dame el lado A del triángulo: "))
b=int(input("Dame el lado B del triángulo: "))
c=int(input("Dame el lado C del triángulo: "))
perímetro = a+b+c
print("El perímetro del triángulo es de ",perímetro," metros.")
###############################Triángulo
pausa()

###############################Rectangulo
print("Ahora toca calcular el área y el perímetro de un rectangulo")
base2 = int(input("Dame la base del rectangulo:"))
altura2 = int(input("Dame la altura del rectangulo:"))
arear = (base2*altura2)
perímetror = (base2+altura2)*2
print("El area del rectangulo es ", arear," y su perimetro es ", perímetror)

###############################Rectangulo
pausa()
##############################Pendiente
print("A continuacion se va a calcular la pendiente de (2,2) y (6,10)")
x1,x2,y1,y2 = 2,6,2,10
m = y2-y1/x2-x1
print("La pendiente de (2,2) y (6,10) es: ",m)
##############################Pendiente
pausa()

##############################Funcion
print("Determina (y) con la siguiente formula: (y = x^2 + 6x + 9)")
x= int(input("Dame el valor de X: "))
y= (x**2) + 6*x + 9
print("El valor de y es: ",y)
##############################Funcion

pausa()

##############################Comparaciones
print("La longitud de la palabra python es de: ",len("python"), " caracteres")
print("La longitud de la palabra dragon es de: ",len("dragon"), " caracteres")
print("Es falso que dragon tenga mas caracteres que python: ",len('python') > len('dragon'))  # False
print("Ahora se va a checar si |on| se encuentra en las 2 palabras (python y dragon)")
print('python:', 'on' in 'python')  
print('dragon:', 'on' in 'dragon')  
print("Se va a checar si |jargon| esta en la frase |I hope this course is not full of jargon.|")
print('jargon' in 'I hope this course is not full of jargon.')
print("Ahora se va a negar que |on| no es python o dragon")
print('python:', 'on' is  'python')  
print('dragon:', 'on' is  'dragon')  
print("Se va a convertir el valor de la longitud de |python| en un valor flotante y luego a un valor string")
python = "python"
python = float(len(python))
print(type(python))
print('Variable float = ', python)
pausa()
print("Ahora se va a convertir dicha variable a string...")
python = str(python)
print(type(python))
print('Variable string =', python)
pausa()

print("Dame un numero, para determinar si es par o no...")
num = int(input("Dame un numero: "))
if (num % 2) == 0:
   print("{0} es par".format(num))
else:
   print("{0} es impar".format(num))
pausa()
print("Se va a comparar si (7//3) es igual a 2.7")
floor = 7//3
ent = 2.7
print(floor == ent)

pausa()
print("Se va a comparar si ´10´ es igual a 10")
print("10" == 10)

pausa()
print("Se va a comparar si ´9.8´ es igual a 10")
print("9.8" == 10)

pausa()
print("Se va a calcular el salario semanal de una persona en base a su sueldo por hora")
horas = int(input("Dame las horas que trabaja por dia: "))
salario= float(input("Dame cuanto gana por hora trabajada: "))
dias = int(input("Cuantos dias trabaja: "))
print("El salario de la persona es de ",round(horas*salario*dias,2), " pesos semanales")
pausa()
print("Se va a calcular los segundos que tienes viviendo en base a tus años de vida...")
años = float(input("Dame los años que tienes: "))
print("Tienes unos ",años*365*24*60*60, " segundos vividos.... que viejo.")
pausa()
print("Se van a mostrar unos datos amontonados en cierto orden...")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
##############################Comparaciones
