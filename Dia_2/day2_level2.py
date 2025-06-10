import math
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
print("La división modular de ", number_one, " y ", number_two, "es: ", remainder)
print("La potencia del numero ", number_one, " elevado a ", number_two, "es: ", exp)
print("La floor division de ", number_one, " y ", number_two, "es: ", floor_division)
print("A continuacion se va a calcular el area y la circuferencia de un circulo de radio de 30 metros")
radio = 30
Area = math.pi*(radio*radio)
Circu = math.pi*(radio*2)
print("El area del circulo es de ", round(Area,2), " metros, mientras que su circunferencia es de ", round(Circu,2), " metros")
print("Ahora es tu turno de determinar el radio del circulo...")
radio_2 = int(input("Dame el radio del circulo: "))
Area_2 = math.pi*(radio_2*radio_2)
Circu_2 = math.pi*(radio_2*2)
print("El area del circulo en base al radio puesto es de ", round(Area_2,2), " metros, mientras que su circunferencia es de ", round(Circu_2,2), " metros")

firstname = input("Dame tu primer nombre: ")
lastname = input("Dame tu apellido: ")
country = input("Dame tu pais de origen: ")
print("Eres ", firstname, " ", lastname, ", ", "eres del pais de ", country)
##################### Ejercicios nivel 2.