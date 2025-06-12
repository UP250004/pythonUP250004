import math
#IDENTIFICACION DEL DATO INTRODUCIDO...#
print("El dato 10 es un entero: ",type(10))          # Int
print("El dato 9.8 es un float: ",type(9.8))        # Float
print("El dato (4 +4j) es un complejo: ",type(4 + 4j))      # Complex number
print("Los elementos en un corchete conforman una lista [Asabeneth, Python, Finland] es una lista...",type(['Asabeneh', 'Python', 'Finland']))  # Lista
print("Tu nombre ", firstname," es un dato tipo string... ",type(firstname))   # String
print("Tu apellido ", lastname, " es un dato tipo string...",type(lastname)) # String
print("Tu país", country,"es un dato tipo string...",type(country))    # String
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

#IDENTIFICACION DEL DATO INTRODUCIDO...#

#PROBLEMA MATEMÁTICO DE LA DISTANCIA EUCLIDIANA (PITÁGORAS)#
print("A continuacion se va a resolver un problema euclidiano con Pitágoras con las coordenadas (2,3) y (10,8)")
x1 = 2
y1 = 3
x2 = 10
y2 = 8
xr = x2 - x1
yr = y2 - y1
resultado = math.sqrt((xr*xr)+(yr*yr))
print("El resultado de la operación es: ", round(resultado,2))


#PROBLEMA MATEMÁTICO DE LA DISTANCIA EUCLIDIANA (PITÁGORAS)#