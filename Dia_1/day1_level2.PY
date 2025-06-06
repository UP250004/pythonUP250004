import math

#OPERACIÓN MATEMÁTICAS...#
def operaciones():
        print("Hello world\n")
        print("Calculadora perrona")
        print("Suma..............1")
        print("Resta.............2")
        print("Multiplicacion....3")
        print("Division..........4")
        print("Exponencial.......5")
        print("Modular...........6")
        print("Piso..............7")
        case = int(input("¿Que operacion quieres realizar?: "))
        if case== 1:
                a=int(input("Inserte el número 1: "))
                print("\n")
                b=int(input("Inserte el número 2: "))

                print("La suma de los 2 números da: ")
                print(a+b)
        elif case == 2:
                a=int(input("Inserte el número positivo: "))
                b=int(input("Inserte el número negativo: "))

                print("La resta de los 2 números da: ")
                print(a-b)
        elif case == 3:
                a=int(input("Inserte el número 1: "))
                b=int(input("Inserte el número 2: "))

                print("La multiplicacion de los 2 números da: ")
                print(a*b)
        elif case == 4:
                a=int(input("Inserte el número 1: "))
                b=int(input("Inserte el número 2: "))

                print("La division de los 2 números da: ")
                print(round(a/b))
        elif case == 5:
                a=int(input("Inserte el número base: "))
                print("\n")
                b=int(input("Inserte el exponente: "))
                print("El numero exponenciado da: ")
                print(a**b)
        elif case == 6:
                a=int(input("Inserte el número 1: "))
                print("\n")
                b=int(input("Inserte el número 2: "))
                print("El modular da: ")
                print(a%b)
        elif case == 7:
                a=int(input("Inserte el número 1: "))
                b=int(input("Inserte el número 2: "))
                print("El floor da: ")
                print(a//b)
        else:
                print("Default case")
operaciones()
#OPERACIÓN MATEMÁTICAS...#

#NOMBRES#
firstname = input("Dame tu primer nombre: ")
lastname = input("Dame tu apellido: ")
country = input("Dame tu pais de origen: ")
print("Eres ", firstname, " ", lastname, ", ", "eres del pais de ", country, " y estas disfrutando de los 30 dias de programar en python...")
#NOMBRES#

#IDENTIFICACION DEL DATO INTRODUCIDO...#
print("El dato 10 es un entero: ",type(10))          # Int
print("El dato 9.8 es un float: ",type(9.8))        # Float
print("El dato (4 +4j) es un complejo: ",type(4 + 4j))      # Complex number
print("Los elementos en un corchete conforman una lista [Asabeneth, Python, Finland] es una lista",type(['Asabeneh', 'Python', 'Finland']))  # Lista
print(type(firstname))   # String
print(type(lastname)) # String
print(type(country))    # String
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

#IDENTIFICACION DEL DATO INTRODUCIDO...#

#PROBLEMA MATEMÁTICO DE LA DISTANCIA EUCLIDIANA (PITÁGORAS)#
print("A continuacion se va a resolver un problema euclidiano con Pitágoras")
x1 = int (input("Dame la coordenada x1: "))
y1 = int (input("Dame la coordenada Y1: "))
x2 = int (input("Dame la coordenada X2: "))
y2 = int (input("Dame la coordenada Y2: "))
xr = x2 - x1
yr = y2 - y1
resultado = math.sqrt((xr*xr)+(yr*yr))
print("El resultado de la operación es: ", round(resultado,2))


#PROBLEMA MATEMÁTICO DE LA DISTANCIA EUCLIDIANA (PITÁGORAS)#